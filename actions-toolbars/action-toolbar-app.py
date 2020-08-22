import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Actions Toolbar App")

        label = QLabel("Sample Label Content")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        toolbar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.addToolBar(toolbar)

        action_button1 = QAction(QIcon("cell-phone.png"), "Custom Button 1",
                                 self)
        action_button1.setStatusTip("Status tip.")
        action_button1.triggered.connect(self.onActionButtonClicked)
        action_button1.setCheckable(True)
        toolbar.addAction(action_button1)

        toolbar.addSeparator()

        action_button2 = QAction(QIcon("cell-phone.png"), "Custom Button 2",
                                 self)
        action_button2.setStatusTip("Status tip.")
        action_button2.triggered.connect(self.onActionButtonClicked)
        action_button2.setCheckable(True)
        toolbar.addAction(action_button2)

        toolbar.addSeparator()

        toolbar.addWidget(QLabel("Toolbar Label"))
        toolbar.addWidget(QCheckBox())

        statusbar = QStatusBar(self)
        self.setStatusBar(statusbar)

    def onActionButtonClicked(self, s):
        print("Action Button Clicked!!", s)


def test_app_driver(*args, **kwargs):
    app = QApplication(*args, **kwargs)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    test_app_driver(sys.argv)
