"""Loads user config from config/local.toml."""
import tomllib
from pathlib import Path


DEFAULTS = {
    "aimbot": {"enabled": False, "fov": 8.0, "smoothing": 0.35},
    "esp": {"enabled": False, "show_names": True, "show_skeleton": False},
    "wallhack": {"enabled": False},
    "bypass": {"jitter": True},
}


def load_config(path: str = "config/local.toml") -> dict:
    p = Path(path)
    if not p.exists():
        return DEFAULTS
    with p.open("rb") as f:
        user = tomllib.load(f)
    merged = {**DEFAULTS}
    for section, values in user.items():
        merged.setdefault(section, {}).update(values)
    return merged