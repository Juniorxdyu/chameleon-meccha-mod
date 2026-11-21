# Offset guide

Meccha Chameleon offsets live in `offsets/chameleon_offsets.json`.
The file is versioned by game build — if you update it, bump `game_version`.

## Key modules

| key | meaning |
|-----|---------|
| `player_base` | base pointer to local player struct |
| `entity_list` | array of entity pointers (stride 0x8) |
| `view_matrix` | 4x4 float matrix for world-to-screen |
| `camera_ptr` | camera origin |
| `world_to_screen` | game's own w2s function |

## Updating after a patch

1. Run `python scripts/dump_offsets.py`
2. Diff against old file
3. Test ESP first (visual, low risk) before enabling aimbot
4. Push to `dev` branch