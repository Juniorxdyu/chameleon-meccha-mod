# Security Policy

## Scope

`chameleon-meccha-mod` is a cheat/overlay tool for the game **Meccha Chameleon**.
It reads game memory, hooks D3D11, and injects a DLL payload. Because of that:

- Do **not** run this on accounts you care about.
- Do **not** use it on official servers — you will get banned.
- The loader will refuse to start if `MecchaChameleon.exe` is not detected.

## Reporting a vulnerability

If you find a bug that could crash the game, corrupt saves, or trigger anti-cheat
detection, please open a **private security advisory** on GitHub. Do not post it
in issues or Discord.

We aim to respond within 72 hours.

## Known anti-cheat surface

The following are **expected** to be flagged by Meccha Chameleon's AC:

- `aimbot` module active
- `esp` module active during ranked
- `injector` writing to `.text` of the game process

The `bypass` folder contains experimental anti-detection stubs. Use at your own risk.

## Disclaimer

This project is provided for educational and modding-community purposes only.
The maintainers are not responsible for bans, damage, or ToS violations.