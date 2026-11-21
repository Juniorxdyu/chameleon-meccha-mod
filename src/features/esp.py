"""ESP overlay handler — box, skeleton and name tags for entities."""
from dataclasses import dataclass
from src.core.memory_bridge import MemoryBridge
from src.core.w2s import world_to_screen


@dataclass
class Entity:
    address: int
    world_pos: tuple[float, float, float]
    health: int
    is_chameleon: bool


class EspHandler:
    name = "esp"

    def __init__(self, bridge: MemoryBridge, config: dict):
        self.bridge = bridge
        self.max_entities = config.get("max_entities", 128)
        self.render_offset = int(config["render_offset"], 16)

    def install(self) -> None:
        self.bridge.write_int(self.bridge.resolve(hex(self.render_offset)), 1)

    def collect_entities(self, entity_list_base: int) -> list[Entity]:
        entities: list[Entity] = []
        for i in range(self.max_entities):
            addr = self.bridge.read_int(entity_list_base + i * 0x8)
            if addr == 0:
                continue
            pos = self.bridge.read_vec3(addr + 0x134)
            hp = self.bridge.read_int(addr + 0x1A0)
            flag = self.bridge.read_int(addr + 0x2C8) == 1
            entities.append(Entity(addr, pos, hp, flag))
        return entities

    def project(self, entities: list[Entity], view_matrix: list[float], w: int, h: int) -> list[tuple[float, float]]:
        out = []
        for e in entities:
            pt = world_to_screen(view_matrix, e.world_pos, w, h)
            if pt:
                out.append(pt)
        return out