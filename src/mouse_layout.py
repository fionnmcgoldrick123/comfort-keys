from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QComboBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

#right widget
right = QWidget()
right_layout = QVBoxLayout()
right.setLayout(right_layout)

right_label = QLabel()
right_img = QPixmap("./assets/imgs/mouse.png")
right_img = right_img.scaled(70,70, Qt.KeepAspectRatio, Qt.SmoothTransformation)
right_label.setPixmap(right_img)
right_label.setFixedSize(200,140)
right_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

right_combo = QComboBox()
right_combo.setCurrentIndex(-1) # No default selection
right_combo.setStyleSheet("font-size: 16px;")
right_combo.setPlaceholderText("Select Device")
right_combo.currentTextChanged.connect(print) # Print selected device to console

right_layout.addWidget(right_label)
right_layout.addWidget(right_combo)