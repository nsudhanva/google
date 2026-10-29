# google

Flashcards for the 793 LeetCode problems Google asked in the last six months, with filters for
the 452 asked in the last 3 months and the 154 asked in the last 30 days. Read the problem,
guess its topics, open a hint if you are stuck, then check a short solution approach written in
ASD-STE100 Simplified Technical English. Every page fits one screen: long statements shrink, then
split into pages. Search finds any problem by LeetCode number, title, topic or statement text.
Progress lives in SQLite; a background scorer tracks how ready you are.

```
.
├── pyproject.toml       # Python tools (uv, Python 3.15): data ingest + approach lint
├── src/google/          # `uv run google ingest | check`
├── data/
│   ├── problems.json    # built by `uv run google ingest` (lists, ranks, frequency, statements)
│   ├── approaches.json  # one ASD-STE100 approach and hint per problem
│   ├── approach-reviews.json  # review trail for every approach
│   └── progress.db      # your progress (SQLite, git-ignored)
├── web/                 # TanStack Start app (React, Vite, Tailwind, shadcn/ui)
├── Dockerfile, docker-compose.yml, Caddyfile
├── deploy/              # systemd timer that keeps the server on the latest images
└── .zed/                # Zed settings, debug configs, tasks
```

## Run it

```bash
docker compose up -d --build     # then open http://google.localhost
```

Caddy serves the app at `http://google.localhost` on port 80 (plain HTTP, so there is no
certificate to trust). Chrome, Firefox and curl resolve `*.localhost` to 127.0.0.1 by themselves;
Safari needs `127.0.0.1 google.localhost` in `/etc/hosts`. If port 80 is taken, run with
`HTTP_PORT=8080` and open `http://google.localhost:8080`. Set `TZ` (for example
`TZ=America/Los_Angeles`) so day streaks roll over at your midnight. Progress persists in the
`progress` volume. `docker-compose.override.yml` builds the images locally; without it, compose
runs the published ones.

## Deploy (live at https://google.sudhanva.me)

Built for the smallest machines; it runs on a free GCP e2-micro (1 GB RAM) with room to spare.

- **Images** (published to GHCR by `.github/workflows/images.yml` on every push to `main`):
  `google-web` is the bare `node` binary on Alpine with a self-contained 2 MB server bundle
  (`ssr.noExternal`, no `node_modules` but `srvx`) and a 64 MB heap cap, about 20 to 130 MB of
  RAM under load. `google-caddy` is Caddy with the static files baked in, precompressed with
  brotli, zstd and gzip, and served with year-long immutable caching.
- **Server**: put `docker-compose.yml` in `/opt/google-cards` with a `.env` holding
  `SITE_ADDRESS=google.sudhanva.me`, `BIND=0.0.0.0` and `TZ=...`, then run
  `docker compose up -d`. Caddy gets the HTTPS certificate itself; the DNS record is a plain
  (not proxied) A record.
- **Continuous deployment**: the systemd timer in `deploy/` runs every 5 minutes, pulls new
  images from GHCR and recreates only the containers that changed, so a push to `main` is live
  within about 10 minutes. Install it with
  `sudo cp deploy/google-cards-update.* /etc/systemd/system/ && sudo systemctl enable --now google-cards-update.timer`.
- **GCP**: e2-micro and a 30 GB standard disk in `us-central1` (Always Free), a static IP in use
  by that VM, and a firewall rule for 80/443. Keep the VM running: a reserved IP is only free
  while attached.

## Develop

```bash
uv sync && bun install
bun run dev          # http://localhost:3000, progress in data/progress.db
bun run check        # Biome lint + format check (bun run fix to apply)
bun run typecheck    # tsc
bun run test         # Vitest unit tests: scheduler, scorer, search
bun run test:e2e     # builds, starts the server on a throwaway DB, tests the HTTP API
uv run ruff check && uv run ruff format --check && uv run ty check
```

## How it works

- **Data** (`src/google/ingest.py`): the problem lists, ranks, frequency and topics come from
  [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems)
  (Google: 30 days, 3 months, 6 months). Each problem stores its rank and frequency for every
  period it appears in; the study page and the Problems page filter and sort by period. Statements come from [doocs/leetcode](https://github.com/doocs/leetcode)
  (CC BY-SA 4.0) and are allowlist-sanitized. Premium statements are left out.
- **Approaches and hints** (`data/approaches.json`): Claude agents wrote one approach and one hint
  per problem. A second set of Claude agents reviewed each approach against the statement and the
  doocs reference solution. Codex CLI gave an independent second opinion on every approach and
  on 550 of the 793 hints (it ran out of credits; a separate strict Claude reviewer covered the
  other 243 hints). A Claude pass adjudicated every disagreement, and Codex rechecked the approach fixes
  (`data/approach-reviews.json` keeps the trail). `uv run google check` enforces the mechanical
  rules: ASD-STE100 sentence limits, no unapproved words, one big-O each, and hints that never
  name the problem's technique tags.
- **Search** (`web/src/lib/search.ts`): LeetCode number (`1`, `#1`, `lc 1`), title words and
  prefixes, acronyms (`lis`), one- or two-letter typos, difficulty, topics and statement text.
  Every word must match; ties go to the problem Google asks more often. Press `/` or ⌘K anywhere.
- **Scheduling** (`web/src/lib/scheduler.ts`): Leitner boxes replayed from the attempt log.
  *Visit again* returns a card in 10 minutes and puts it on the visit-again list. *Got it* moves it
  up one box (1, 3, 7, 16, 35, 90 days). *Visit less often* jumps two boxes and doubles the wait.
  *Skip* defers a card for an hour without grading it.
- **Scoring** (`web/src/lib/scorer.ts`, `web/src/server/scorer.ts`): each graded card scores half
  topic F1 (less a quarter for each hint opened), half your grade. Mastery fades with time since the last review. Readiness is mastery
  weighted by Google frequency. The server recomputes it after every attempt and every 15 minutes,
  and stores one point per day for the trend line.
- **Backend** (`web/src/server/`): plain service functions over `node:sqlite`, exposed twice as
  thin wrappers: TanStack Start server functions for the UI and a JSON API for scripts. The
  attempt log is the only state: card state, lists and scores are all derived from it, so
  clearing progress is a delete. Your own answers ("My answer") live in a separate `notes` table,
  so clearing progress keeps them.

## API

| Method and path | Does |
| --- | --- |
| `GET /api/search?q=two+sum&limit=10` | Ranked problems for a free-text query |
| `GET /api/problems` | Every problem with its progress (no topics) |
| `GET /api/problems/:slug` | One full card: statement, topics, approach, hints, state |
| `GET /api/deck?period=30d&set=again&topic=Graph+Theory&difficulty=Hard` | The next card in a study set |
| `POST /api/attempts` `{slug, grade, guessed, hints}` | Grade (`again`, `good`, `less`) or `skip` a card |
| `PUT /api/notes` `{slug, text}` | Save your own answer to a problem (empty text deletes it) |
| `DELETE /api/progress?slug=two-sum` or `?all=true` | Clear one problem, or everything |
| `GET /api/report` | Readiness, coverage, accuracy, streak, weak topics, daily trend |

Bad input returns 400 with the validation issues; an unknown problem returns 404.

## Keys

`Enter` show answer, `H` hint, `S` skip, `1` visit again, `2` got it, `3` visit less often,
`B` back (hides the answer, or goes to the previous card), `M` my answer, `←`/`→` statement pages, `/` or ⌘K
search.
