import sys # For command-line arguments to Qt

from PySide6.QtWidgets import (
    QApplication,  # core Qt app loop
    QMainWindow,   # main app window
    QWidget,       # generic container
    QVBoxLayout,   # layout manager
    QLabel         # simple text label
)

from PySide6.QtCore import Qt 

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Comfort Keys")

#central widget / layout
central = QWidget()
layout = QVBoxLayout()
central.setLayout(layout)

#centered header for application
header = QLabel("comfort-keys")
header.setStyleSheet("font-size: 24px;")
header.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
layout.addWidget(header)

#window configuration
window.setCentralWidget(central)
window.setFixedSize(400,200)
window.show()

sys.exit(app.exec())