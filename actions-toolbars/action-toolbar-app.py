import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Actions Toolbar App")

        label = QLabel("Sample Label Content")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)


def test_app_driver(*args, **kwargs):
    app = QApplication(*args, **kwargs)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    test_app_driver(sys.argv)
