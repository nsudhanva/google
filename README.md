# google

A Python package (uv, Python 3.15) and a TanStack Start web app (bun) in one repo.

```
.
├── pyproject.toml   # Python project, ruff + ty config
├── src/google/      # Python package (`uv run google` / `python -m google`)
├── package.json     # bun workspace root, Biome
├── biome.json       # JS/TS lint + format
├── web/             # TanStack Start app (React, Vite, Tailwind)
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
```

## Zed

Open the repo root in Zed. Project settings in `.zed/` give you:

- **Python**: ty (types) + Ruff (lint, format on save, import sorting), from `.venv`.
- **Debugging**: F4 → "Python: google (module)" or "Python: current file" (debugpy from `.venv`).
- **TS/TSX**: vtsls + Biome (format on save, fix-all, import sorting). Requires the Biome extension
  (`zed: extensions` → Biome).
- **Tasks**: `task: spawn` → web dev server, checks, etc.
