"""PyQt6 transparent overlay window for ESP + menu."""
import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtWidgets import QApplication, QWidget


class OverlayWindow(QWidget):
    def __init__(self, bridge, handlers):
        super().__init__()
        self.bridge = bridge
        self.handlers = {h.name: h for h in handlers}
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(0, 0, 1920, 1080)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(16)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        pen = QPen(QColor(0, 255, 128, 220), 2)
        painter.setPen(pen)

        esp = self.handlers.get("esp")
        if esp:
            for x, y in [(960, 540)]:
                painter.drawRect(int(x) - 20, int(y) - 40, 40, 80)

    def run(self) -> None:
        app = QApplication.instance() or QApplication(sys.argv)
        self.show()
        sys.exit(app.exec())