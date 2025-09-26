import sys # For command-line arguments to Qt

from PySide6.QtWidgets import (
    QApplication,  # core Qt app loop
    QMainWindow,   # main app window
    QWidget,       # generic container
    QVBoxLayout,   # vertical layout manager
    QHBoxLayout    # horizontal layout manager
)

from PySide6.QtCore import Qt 

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Comfort Keys")

#central widget / layout
central = QWidget()
main_layout = QVBoxLayout()
central.setLayout(main_layout)

# import header from separate file
from header import header
main_layout.addWidget(header)

row = QHBoxLayout()

#left widget
left = QWidget()
left.setStyleSheet("background-color: lightblue; border: 1px solid black;")
left.setFixedSize(200,140)

#right widget
right = QWidget()
right.setStyleSheet("background-color: lightblue; border: 1px solid black;")
right.setFixedSize(200,140)

#layout configuration
row.addWidget(left)
row.addWidget(right)

main_layout.addLayout(row)

#window configuration
window.setCentralWidget(central)
window.setStyleSheet("background-color: lightblue;")
window.setFixedSize(400,200)
window.show()

sys.exit(app.exec())