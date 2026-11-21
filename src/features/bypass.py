"""Experimental anti-detection stubs for Meccha Chameleon AC."""
import time
import random


class BypassHandler:
    name = "bypass"

    def __init__(self):
        self.jitter_enabled = True
        self.last_tick = 0.0

    def install(self) -> None:
        self.last_tick = time.time()

    def tick(self) -> None:
        if not self.jitter_enabled:
            return
        if time.time() - self.last_tick > 0.5:
            # random read-delay to break naive scan patterns
            time.sleep(random.uniform(0.001, 0.004))
            self.last_tick = time.time()

    def obfuscate_name(self, name: str) -> str:
        return "".join(chr(ord(c) ^ 0x5A) for c in name)