"""In-overlay cheat menu — toggles aimbot/esp/wallhack."""
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QLabel
from PyQt6.QtCore import Qt


class CheatMenu(QWidget):
    def __init__(self, handlers: dict):
        super().__init__()
        self.handlers = handlers
        self.setWindowFlags(Qt.WindowType.Tool | Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowTitle("Meccha Chameleon Cheats")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("chameleon-meccha-mod"))
        for name, h in handlers.items():
            cb = QCheckBox(name)
            cb.setChecked(False)
            cb.stateChanged.connect(lambda s, n=name: self._toggle(n, s))
            layout.addWidget(cb)
        self.setLayout(layout)

    def _toggle(self, name: str, state: int) -> None:
        h = self.handlers[name]
        if state == Qt.CheckState.Checked.value and hasattr(h, "enable"):
            h.enable()
        elif hasattr(h, "disable"):
            h.disable()