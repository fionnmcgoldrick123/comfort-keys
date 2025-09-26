from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QComboBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

#left widget
left = QWidget()
left_layout = QVBoxLayout()
left.setLayout(left_layout)

left_label = QLabel()
left_img = QPixmap("./assets/imgs/keyboard.png")
left_img = left_img.scaled(90,80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
left_label.setPixmap(left_img)
left_label.setFixedSize(200,140)
left_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

combo = QComboBox()
combo.addItems(["Select Layout", "QWERTY", "AZERTY", "DVORAK", "COLEMAK"])
combo.setCurrentIndex(-1) # No default selection
combo.setStyleSheet("font-size: 16px;")
combo.setPlaceholderText("Select Layout")
combo.currentTextChanged.connect(print) # Print selected layout to console

left_layout.addWidget(left_label)
left_layout.addWidget(combo)