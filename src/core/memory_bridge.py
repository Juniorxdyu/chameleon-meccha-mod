"""Thin wrapper over pymem for reading/writing Meccha Chameleon memory."""
import pymem
import pymem.process


class MemoryBridge:
    def __init__(self, pid: int):
        self.pid = pid
        self.pm: pymem.Pymem | None = None
        self.base: int = 0

    def attach(self) -> None:
        self.pm = pymem.Pymem()
        self.pm.open_process_from_id(self.pid)
        module = pymem.process.module_from_name(
            self.pm.process_handle, "MecchaChameleon.exe"
        )
        if module is None:
            raise RuntimeError("MecchaChameleon.exe module not found")
        self.base = module.lpBaseOfDll

    def read_int(self, address: int) -> int:
        return self.pm.read_int(address)

    def read_float(self, address: int) -> float:
        return self.pm.read_float(address)

    def read_vec3(self, address: int) -> tuple[float, float, float]:
        raw = self.pm.read_bytes(address, 12)
        import struct
        return struct.unpack("<fff", raw)

    def write_float(self, address: int, value: float) -> None:
        self.pm.write_float(address, value)

    def resolve(self, offset_hex: str) -> int:
        return self.base + int(offset_hex, 16)