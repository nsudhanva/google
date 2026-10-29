# syntax=docker/dockerfile:1
# Two small images for small machines (built for a 1 GB e2-micro):
#   web   - the node binary on Alpine, running the self-contained server bundle; it keeps a
#           copy of the static files for the moments when Caddy runs a different build
#   caddy - Caddy with the static files baked in, compressed ahead of time
# Build one with `docker build --target web|caddy .`; CI publishes both to GHCR.

FROM oven/bun:1.3 AS build
WORKDIR /app
COPY package.json bun.lock ./
COPY web/package.json web/
RUN bun install --frozen-lockfile --ignore-scripts
COPY web web
RUN bun run build \
	&& mkdir -p /out/node_modules \
	&& cp -rL web/node_modules/srvx /out/node_modules/srvx \
	&& cp -r web/dist/server /out/server \
	&& cp -r web/dist/client /out/client

# Compress once at build time so Caddy serves .br/.zst/.gz files without spending CPU.
FROM alpine:3.22 AS static
RUN apk add --no-cache brotli zstd
COPY --from=build /app/web/dist/client /srv
RUN find /srv -type f \( -name '*.js' -o -name '*.css' -o -name '*.svg' \) \
	-exec gzip -9 -k {} \; -exec brotli -q 11 -k {} \; -exec zstd -19 -q -k {} \;

FROM caddy:2-alpine AS caddy
LABEL org.opencontainers.image.source=https://github.com/nsudhanva/google
COPY --from=static /srv /srv
COPY Caddyfile /etc/caddy/Caddyfile

# Only the node binary on plain Alpine: no npm, yarn or corepack.
FROM alpine:3.22 AS web
LABEL org.opencontainers.image.source=https://github.com/nsudhanva/google
RUN apk add --no-cache libstdc++ \
	&& addgroup -S node && adduser -S -G node node
COPY --from=node:24-alpine /usr/local/bin/node /usr/local/bin/node
ENV NODE_ENV=production \
	PORT=3000 \
	DATA_DIR=/app/data \
	DATABASE_PATH=/state/progress.db \
	NODE_OPTIONS="--max-old-space-size=64 --max-semi-space-size=1"
WORKDIR /app
COPY --from=build /out ./
COPY data/problems.json data/approaches.json data/
RUN mkdir -p /state && chown node:node /state
USER node
EXPOSE 3000
CMD ["node", "node_modules/srvx/bin/srvx.mjs", "serve", "--prod", "--entry", "server/server.js", "--static", "../client", "--port", "3000"]
