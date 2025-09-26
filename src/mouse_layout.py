from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

right = QWidget()
right_layout = QVBoxLayout(right)
right_layout.setContentsMargins(0, 0, 0, 0)
right_layout.setSpacing(6)

right_label = QLabel()
right_img = QPixmap("./assets/imgs/mouse.png").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
right_label.setPixmap(right_img)
right_layout.addWidget(right_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

right_combo = QComboBox()
right_combo.setStyleSheet("font-size: 16px;")
right_combo.setPlaceholderText("Select Device")
right_combo.setCurrentIndex(-1)
right_layout.addWidget(right_combo, alignment=Qt.AlignTop | Qt.AlignHCenter)
