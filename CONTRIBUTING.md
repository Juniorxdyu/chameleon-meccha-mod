# Contributing to chameleon-meccha-mod

Thanks for wanting to help with the Meccha Chameleon Cheats project.

## Setup

```bash
git clone https://github.com/community/chameleon-meccha-mod
cd chameleon-meccha-mod
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Run the loader:

```bash
python -m src.bootstrap.launch --profile dev
```

## Branching

- `main` — stable offsets, tested against current Meccha Chameleon build
- `dev` — bleeding edge, offsets may be broken
- `feature/*` — new cheats, esp variants, aimbot tweaks

## Offset updates

When Meccha Chameleon patches, `offsets/chameleon_offsets.json` will go stale.
Update via:

```bash
python scripts/dump_offsets.py --process MecchaChameleon.exe
```

Then open a PR with the diff.

## Code style

- Python 3.11+, `ruff` for linting
- Keep memory reads in `src/core/` — never in UI layer
- New cheats go under `src/features/` with a matching test in `tests/`

## Reporting bugs

Open an issue with: build hash, offset file used, and a short clip of the bug.

## Legal

This is for single-player / private-server use only. Do not use on official Meccha Chameleon servers. See SECURITY.md.