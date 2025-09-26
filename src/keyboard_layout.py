from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

keyboard_layout = QWidget()
left_layout = QVBoxLayout(keyboard_layout)
left_layout.setContentsMargins(0, 0, 0, 0)
left_layout.setSpacing(6)

left_label = QLabel()
left_img = QPixmap("./assets/imgs/keyboard.png").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
left_label.setPixmap(left_img)

# Center the LABEL inside the column:
left_layout.addWidget(left_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

combo = QComboBox()
combo.addItems(["Select Layout", "QWERTY", "AZERTY", "DVORAK", "COLEMAK"])
combo.setCurrentIndex(-1)  # No default selection (ok if you're on Qt ≥ 6.7 with placeholder)
combo.setStyleSheet("font-size: 16px;")
combo.setPlaceholderText("Select Layout")

# Center the COMBO too:
left_layout.addWidget(combo, alignment=Qt.AlignTop | Qt.AlignHCenter)
