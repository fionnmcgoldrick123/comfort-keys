import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from set_sound import load_sounds

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Comfort Keys")

load_sounds(parent=window) # Load sound effects at application start

central = QWidget()
main_layout = QVBoxLayout(central)
main_layout.setContentsMargins(12, 12, 12, 12)
main_layout.setSpacing(8)

# Header
from header import header
main_layout.addWidget(header)

# Row with two columns
row = QHBoxLayout()
row.setContentsMargins(0, 0, 0, 0)
row.setSpacing(12)

from keyboard_layout import keyboard_layout
from mouse_layout import right

# Add ONLY to the row (no duplicates in main_layout)
row.addWidget(keyboard_layout, stretch=1, alignment=Qt.AlignTop)
row.addWidget(right,           stretch=1, alignment=Qt.AlignTop)

# Attach the row to the main_layout
main_layout.addLayout(row)

window.setCentralWidget(central)
window.setStyleSheet("background-color: #B9CBD9")
window.setFixedSize(400, 200)
window.show()

sys.exit(app.exec())
