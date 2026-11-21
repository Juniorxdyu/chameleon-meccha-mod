# Anti-cheat notes

Meccha Chameleon uses a user-mode AC with periodic memory scans.

## Known detection vectors

- Writing to `MecchaChameleon.exe` `.text` — detected
- `CreateRemoteThread` with `LoadLibraryA` — flagged after 30s
- Overlay window class names containing "cheat" — heuristic

## Mitigations in this repo

- `src/features/bypass.py` — random read jitter
- `src/features/spoofer.py` — HWID rotation
- Overlay window class is randomized in `src/renderer/overlay.py`

None of these are guaranteed. Use a throwaway account.