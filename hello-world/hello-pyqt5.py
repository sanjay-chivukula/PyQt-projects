import sys  # Needed to handle exit status of application.

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    pass


def test_app_driver(argv=None):
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    app.exec_()


if __name__ == "__main__":
    test_app_driver(sys.argv)
