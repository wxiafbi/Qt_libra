# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 600)
        self.setWindowTitle("新建窗口")
        self.setAutoFillBackground(True)

        self.push = QPushButton(self)
        self.push.setText('按键')
        self.push.move(300, 300)

        self.qtable = QLabel(self)
        self.qtable.setText("JiuBoy")
        self.qtable.move(300, 200)


if __name__ == "__main__":
    app = QApplication([])
    window = Widget()
    window.show()
    sys.exit(app.exec())
