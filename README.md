# google

A Python package (uv, Python 3.15) and a TanStack Start web app (bun) in one repo.

```
.
├── pyproject.toml   # Python project, ruff + ty config
├── src/google/      # Python package (`uv run google` / `python -m google`)
├── package.json     # bun workspace root, Biome
├── biome.json       # JS/TS lint + format
├── web/             # TanStack Start app (React, Vite, Tailwind, shadcn/ui)
└── .zed/            # Zed settings, debug configs, tasks
```

## Setup

```bash
uv sync        # creates .venv with Python 3.15, ruff, ty, debugpy
bun install    # installs web/ deps and Biome
```

## Python

```bash
uv run google                                  # run
uv run ruff check && uv run ruff format        # lint + format
uv run ty check                                # typecheck
```

## Web

```bash
bun run dev        # http://localhost:3000
bun run build
bun run check      # Biome lint + format check (bun run fix to apply)
bun run typecheck  # tsc
bun run test       # Vitest unit tests
```

The web app is a practice quiz for the Google Hiring Assessment, built with shadcn/ui
(Base UI primitives). Add components with `cd web && bunx shadcn@latest add <name>`;
they land in `web/src/components/ui/`, which Biome leaves alone.

- `web/src/data/`: question bank and sources
- `web/src/lib/`: pure quiz and progress logic (unit tested)
- `web/src/hooks/`: quiz state and keyboard shortcuts
- `web/src/components/`: navbar, theme, quiz UI
- `web/src/routes/`: Practice (`/`), Progress (`/progress`), About (`/about`)

Progress is stored in the browser's localStorage.

## Zed

Open the repo root in Zed. Project settings in `.zed/` give you:

- **Python**: ty (types) + Ruff (lint, format on save, import sorting), from `.venv`.
- **Debugging**: F4 → "Python: google (module)" or "Python: current file" (debugpy from `.venv`).
- **TS/TSX**: vtsls + Biome (format on save, fix-all, import sorting). Requires the Biome extension
  (`zed: extensions` → Biome).
- **Tasks**: `task: spawn` → web dev server, checks, etc.
