"""Locate and attach to the Meccha Chameleon game process."""
import time
import psutil


class ProcessGuard:
    def __init__(self, process_name: str):
        self.process_name = process_name
        self.pid: int | None = None
        self._proc = None

    def wait_for_process(self, timeout: int = 30) -> bool:
        deadline = time.time() + timeout
        while time.time() < deadline:
            for proc in psutil.process_iter(["pid", "name"]):
                if proc.info["name"] == self.process_name:
                    self.pid = proc.info["pid"]
                    self._proc = proc
                    return True
            time.sleep(0.5)
        return False

    def is_alive(self) -> bool:
        return self._proc is not None and self._proc.is_running()

    def module_base(self, module: str) -> int:
        if self._proc is None:
            raise RuntimeError("process not attached")
        for m in self._proc.memory_maps():
            if m.path and m.path.lower().endswith(module.lower()):
                return m.addr
        raise LookupError(f"module {module} not found")