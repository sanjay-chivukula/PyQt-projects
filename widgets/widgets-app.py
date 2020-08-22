import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Checking out QT Widgets")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QDateEdit,
            QTimeEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
        ]

        for widget in widgets:
            layout.addWidget(widget())

        super_widget = QWidget()
        super_widget.setLayout(layout)

        self.setCentralWidget(super_widget)


def test_app_driver(*args, **kwargs):
    app = QApplication(*args, **kwargs)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    test_app_driver(sys.argv)
