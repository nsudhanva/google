#!/bin/sh
# Pulls the latest images and switches to them only when web and caddy come from the same
# commit. A page from one build names asset files that only the same build's Caddy serves.
set -eu
cd /opt/google-cards

docker compose pull --quiet

revision() {
	docker image inspect --format '{{index .Config.Labels "org.opencontainers.image.revision"}}' "$1"
}
web=$(revision ghcr.io/nsudhanva/google-web:latest)
caddy=$(revision ghcr.io/nsudhanva/google-caddy:latest)
if [ "$web" != "$caddy" ]; then
	echo "web is at ${web}, caddy at ${caddy}: waiting for the next run"
	exit 0
fi

docker compose up -d --remove-orphans
docker image prune -f
