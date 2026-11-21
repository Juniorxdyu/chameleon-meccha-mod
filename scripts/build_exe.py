"""PyInstaller build helper for the chameleon-meccha-mod loader."""
import subprocess
import sys
from pathlib import Path


def build() -> int:
    root = Path(__file__).resolve().parent.parent
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--noconsole",
        "--name", "chameleon-meccha-mod",
        "--add-data", f"{root / 'offsets'};offsets",
        str(root / "src" / "bootstrap" / "launch.py"),
    ]
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(build())