import sys  # Needed to handle exit status of application.

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        # Always call the __init__ of QMainWindow, else will result in error.
        super(MainWindow, self).__init__(*args, **kwargs)

        # Derived from QMainWindow class.
        # Sets the title of the Main Window.
        self.setWindowTitle("Hello PyQt5 App")

        label = QLabel("This is label's content")
        label.setAlignment(Qt.AlignCenter)

        # Derived from QMainWindow class.
        # Places a widget in the middle of Main Window.
        # Label is also a widget in PyQt5.
        self.setCentralWidget(label)


def test_app_driver(argv=None):
    app = QApplication(argv)

    window = MainWindow()
    window.show()

    app.exec_()


if __name__ == "__main__":
    test_app_driver(sys.argv)
