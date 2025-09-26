import sys # For command-line arguments to Qt

from PySide6.QtWidgets import (
    QApplication,  # core Qt app loop
    QMainWindow,   # main app window
    QWidget,       # generic container
    QVBoxLayout,   # vertical layout manager
    QHBoxLayout,   # horizontal layout manager
    QLabel,        # display text or image
    QComboBox,     # dropdown selection
)

from PySide6.QtCore import Qt 
from PySide6.QtGui import QPixmap

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

from keyboard_layout import left, combo
main_layout.addWidget(left)

from mouse_layout import right, right_combo
main_layout.addWidget(right)

#layout configuration
row.addWidget(left)
row.addWidget(right)

main_layout.addLayout(row)

#window configuration
window.setCentralWidget(central)
window.setStyleSheet("background-color: #B9CBD9")
window.setFixedSize(400,200)
window.show()

sys.exit(app.exec())