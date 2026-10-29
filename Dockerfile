# syntax=docker/dockerfile:1
# Builds the TanStack Start app with bun, then runs it on Node 24 (for the built-in node:sqlite).

FROM oven/bun:1.3 AS deps
WORKDIR /app
COPY package.json bun.lock ./
COPY web/package.json web/
RUN bun install --frozen-lockfile --production --ignore-scripts

FROM oven/bun:1.3 AS build
WORKDIR /app
COPY package.json bun.lock ./
COPY web/package.json web/
RUN bun install --frozen-lockfile --ignore-scripts
COPY web web
RUN bun run build

FROM node:24-slim
ENV NODE_ENV=production \
    PORT=3000 \
    DATA_DIR=/app/data \
    DATABASE_PATH=/state/progress.db
WORKDIR /app
COPY --from=deps /app/node_modules node_modules
COPY --from=deps /app/web/node_modules web/node_modules
COPY --from=build /app/web/dist web/dist
COPY web/package.json web/
COPY data/problems.json data/approaches.json data/
WORKDIR /app/web
EXPOSE 3000
CMD ["node_modules/.bin/srvx", "serve", "--prod", "--entry", "dist/server/server.js", "--static", "../client", "--port", "3000"]
