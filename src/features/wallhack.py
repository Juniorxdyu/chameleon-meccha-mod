"""Wallhack flag writer for Meccha Chameleon."""
from src.core.memory_bridge import MemoryBridge


class WallhackHandler:
    name = "wallhack"

    def __init__(self, bridge: MemoryBridge, config: dict):
        self.bridge = bridge
        self.flag_offset = int(config["flag_offset"], 16)
        self.active = False

    def install(self) -> None:
        self.enable()

    def enable(self) -> None:
        self.bridge.write_int(self.bridge.resolve(hex(self.flag_offset)), 1)
        self.active = True

    def disable(self) -> None:
        self.bridge.write_int(self.bridge.resolve(hex(self.flag_offset)), 0)
        self.active = False

    def toggle(self) -> bool:
        if self.active:
            self.disable()
        else:
            self.enable()
        return self.active