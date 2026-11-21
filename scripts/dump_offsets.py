"""Dump fresh offsets from a running Meccha Chameleon process."""
import argparse
import json
from pathlib import Path

from src.core.process_guard import ProcessGuard
from src.core.memory_bridge import MemoryBridge


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--process", default="MecchaChameleon.exe")
    ap.add_argument("--out", default="offsets/chameleon_offsets.json")
    args = ap.parse_args()

    guard = ProcessGuard(args.process)
    if not guard.wait_for_process(timeout=10):
        print("process not found")
        return 1

    bridge = MemoryBridge(guard.pid)
    bridge.attach()
    print(f"base = 0x{bridge.base:X}")

    data = json.loads(Path(args.out).read_text())
    data["modules"]["base"] = hex(bridge.base)
    Path(args.out).write_text(json.dumps(data, indent=2))
    print("offsets updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())