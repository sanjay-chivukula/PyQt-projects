import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        color = QColor(color)

        palette = self.palette()
        palette.setColor(QPalette.Window, color)
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


def test_app_driver(*args, **kwargs):
    app = QApplication(*args, **kwargs)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    test_app_driver(sys.argv)
