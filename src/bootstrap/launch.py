"""Entry point for the Meccha Chameleon Cheats loader."""
import argparse
import sys
from pathlib import Path

from src.core.process_guard import ProcessGuard
from src.core.memory_bridge import MemoryBridge
from src.core.offset_loader import OffsetLoader
from src.features.aimbot import AimbotHandler
from src.features.esp import EspHandler
from src.features.wallhack import WallhackHandler
from src.renderer.overlay import OverlayWindow
from src.shared.logger import get_logger

log = get_logger("launch")


def build_handlers(bridge: MemoryBridge, offsets: dict) -> list:
    handlers = []
    handlers.append(AimbotHandler(bridge, offsets["features"]["aimbot"]))
    handlers.append(EspHandler(bridge, offsets["features"]["esp"]))
    handlers.append(WallhackHandler(bridge, offsets["features"]["wallhack"]))
    return handlers


def main() -> int:
    parser = argparse.ArgumentParser(prog="chameleon-meccha-mod")
    parser.add_argument("--profile", default="prod", choices=["dev", "prod"])
    parser.add_argument("--process", default="MecchaChameleon.exe")
    parser.add_argument("--no-overlay", action="store_true")
    args = parser.parse_args()

    guard = ProcessGuard(args.process)
    if not guard.wait_for_process(timeout=30):
        log.error("Meccha Chameleon process not found")
        return 1

    offsets = OffsetLoader(Path("offsets/chameleon_offsets.json")).load()
    bridge = MemoryBridge(guard.pid)
    bridge.attach()

    handlers = build_handlers(bridge, offsets)
    for h in handlers:
        h.install()
        log.info("installed handler %s", h.name)

    if not args.no_overlay:
        overlay = OverlayWindow(bridge, handlers)
        overlay.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())