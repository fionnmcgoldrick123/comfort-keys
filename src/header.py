
import sys # For command-line arguments to Qt

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt 

#centered header for application
header = QLabel("comfort-keys")
header.setStyleSheet("font-size: 24px; color: white;")
header.setContentsMargins(0, 0, 0, 0)
header.setAlignment(Qt.AlignHCenter)
