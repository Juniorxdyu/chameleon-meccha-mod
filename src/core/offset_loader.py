"""Loads the chameleon_offsets.json manifest for the current game build."""
import json
from pathlib import Path


class OffsetLoader:
    def __init__(self, path: Path):
        self.path = path

    def load(self) -> dict:
        if not self.path.exists():
            raise FileNotFoundError(f"offsets not found: {self.path}")
        data = json.loads(self.path.read_text(encoding="utf-8"))
        self._validate(data)
        return data

    def _validate(self, data: dict) -> None:
        required = {"game_version", "modules", "features"}
        missing = required - data.keys()
        if missing:
            raise ValueError(f"offsets missing keys: {missing}")
        for key in ("player_base", "entity_list", "view_matrix"):
            if key not in data["modules"]:
                raise ValueError(f"module offset missing: {key}")

    def current_version(self) -> str:
        return json.loads(self.path.read_text(encoding="utf-8"))["game_version"]