import sys  # Needed to handle exit status of application.

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)  # Create this before using any other GUI objects.

# Creating and configuring the window.
window = QWidget()  # Base class for all UI objects in PyQt.
window.setWindowTitle("PyQt5 App")
window.setGeometry(100, 100, 400, 400)
window.move(10, 10)

# Message to display.
hello_message = QLabel("<h1>Hello World!</h1>", parent=window)
hello_message.move(10, 10)

# Displaying the window.
window.show()

# Exiting the application.
sys.exit(app.exec_())
