# input_listener.py
import keyboard
from PySide6.QtCore import QObject, Signal

class QtBridge(QObject):
    trigger = Signal()  # emitted on any key press

bridge = QtBridge()

def _keyboard_input_listener(event):
    # Called by keyboard lib thread → hop to Qt thread
    bridge.trigger.emit()

def start():
    # Register the global key hook
    keyboard.on_press(_keyboard_input_listener)
