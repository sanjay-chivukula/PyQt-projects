from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def sample_action_slot():
    print("system tray menu action triggered")


app = QApplication([])
app.setQuitOnLastWindowClosed(False)

icon = QIcon("../common-resources/cell-phone.png")

tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()

sample_action = QAction("A Menu Item")
sample_action.triggered.connect(sample_action_slot)
menu.addAction(sample_action)

quit_action = QAction("Quit")
quit_action.triggered.connect(app.quit)
menu.addAction(quit_action)

tray.setContextMenu(menu)

app.exec_()
