import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


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
