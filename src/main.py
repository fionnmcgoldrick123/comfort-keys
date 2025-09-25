import sys # For command-line arguments to Qt

from PySide6.QtWidgets import (
    QApplication,  # core Qt app loop
    QMainWindow,   # main app window
    QWidget,       # generic container
    QVBoxLayout,   # layout manager
    QLabel         # simple text label
)

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("My First PySide6 App")

#central widget / layout
central = QWidget()
layout = QVBoxLayout()
central.setLayout(layout)

label = QLabel("Hello, PySide6!")
layout.addWidget(label)


window.setCentralWidget(central)
window.show()

sys.exit(app.exec())