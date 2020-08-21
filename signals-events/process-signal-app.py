import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QContextMenuEvent
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        val = 5

        self.setWindowTitle("Main Window Title 01")

        # SIGNAL: supposed to call the SLOT self.onWindowTitleChange().
        # Pycharm still doesn't recognize signals,
        # so it will warn/show: Cannot find reference connect in function.
        self.windowTitleChanged.connect(self.onWindowTitleChange)

        # If this calls the self.onWindowTitleChange() then signal-slot works.
        self.setWindowTitle("Main Window Title 02")

        label = QLabel("Label with Content 01")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    # SLOT: to be called with the SIGNAL self.windowTitleChanged.
    @staticmethod
    def onWindowTitleChange(title_string):
        print("Window Title Changed!!!")
        print(title_string)

    # Overriding from QMainWindow, this intercepts the context menu event.
    # The event is fired when the context menu is about to be shown.
    # By overriding, this function will receive events of this type.
    def contextMenuEvent(self, event: QContextMenuEvent):
        print("Context Menu Event, Triggered on mouse right click on Main "
              "Window!!!")
        super(MainWindow, self).contextMenuEvent(event)


def test_app_driver(*args, **kwargs):
    app = QApplication(*args, **kwargs)

    window = MainWindow()
    window.show()

    app.exec_()


if __name__ == "__main__":
    test_app_driver(sys.argv)
