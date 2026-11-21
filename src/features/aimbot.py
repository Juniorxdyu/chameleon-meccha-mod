"""Aimbot handler — target selection + smoothing for Meccha Chameleon."""
import math
from src.core.memory_bridge import MemoryBridge


class AimbotHandler:
    name = "aimbot"

    def __init__(self, bridge: MemoryBridge, config: dict):
        self.bridge = bridge
        self.enabled_offset = int(config["enabled_offset"], 16)
        self.smoothing_offset = int(config["smoothing_offset"], 16)
        self.smoothing = 0.35
        self.fov = 8.0

    def install(self) -> None:
        self.bridge.write_float(
            self.bridge.resolve(hex(self.smoothing_offset)), self.smoothing
        )

    def aim_at(self, target_world: tuple[float, float, float], camera: tuple[float, float, float]) -> tuple[float, float]:
        dx = target_world[0] - camera[0]
        dy = target_world[1] - camera[1]
        dz = target_world[2] - camera[2]
        yaw = math.degrees(math.atan2(dy, dx))
        pitch = math.degrees(math.atan2(-dz, math.hypot(dx, dy)))
        return yaw, pitch

    def in_fov(self, target_yaw: float, current_yaw: float) -> bool:
        delta = abs(((target_yaw - current_yaw + 180) % 360) - 180)
        return delta <= self.fov