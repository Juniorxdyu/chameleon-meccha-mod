"""HWID / session spoofer used before launching Meccha Chameleon."""
import hashlib
import uuid
import winreg


class HwidSpoofer:
    name = "spoofer"

    def __init__(self):
        self.virtual_id = uuid.uuid4().hex

    def install(self) -> None:
        self._write_registry("HwidSeed", self.virtual_id)

    def _write_registry(self, key: str, value: str) -> None:
        try:
            with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\MecchaChameleon\Session",
                0,
                winreg.KEY_SET_VALUE,
            ) as h:
                winreg.SetValueEx(h, key, 0, winreg.REG_SZ, value)
        except OSError:
            pass

    def fingerprint(self) -> str:
        return hashlib.sha256(self.virtual_id.encode()).hexdigest()[:16]