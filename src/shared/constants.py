"""Shared game constants for Meccha Chameleon."""
PROCESS_NAME = "MecchaChameleon.exe"
MODULE_NAME = "MecchaChameleon.exe"
D3D11_DLL = "d3d11.dll"

ENTITY_STRIDE = 0x8
PLAYER_HEALTH_OFFSET = 0x1A0
PLAYER_POS_OFFSET = 0x134
PLAYER_CHAMELEON_FLAG = 0x2C8

DEFAULT_RESOLUTION = (1920, 1080)
OVERLAY_FPS = 60

BANNED_WORDS = {"chameleon", "meccha", "cheat"}  # for name obfuscation stub