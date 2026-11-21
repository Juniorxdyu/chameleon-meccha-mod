import json
from pathlib import Path
from src.core.offset_loader import OffsetLoader


def test_offsets_file_exists():
    p = Path("offsets/chameleon_offsets.json")
    assert p.exists()


def test_offsets_has_required_modules():
    loader = OffsetLoader(Path("offsets/chameleon_offsets.json"))
    data = loader.load()
    for key in ("player_base", "entity_list", "view_matrix"):
        assert key in data["modules"]


def test_offsets_features_present():
    data = json.loads(Path("offsets/chameleon_offsets.json").read_text())
    assert "aimbot" in data["features"]
    assert "esp" in data["features"]