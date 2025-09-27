from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl, QObject
from pathlib import Path

SOUNDS: dict[str, QSoundEffect] = {}
CURRENT_SOUND: QSoundEffect | None = None
SOUNDS_PATH = Path("./assets/sounds")

def load_sounds(parent: QObject | None = None):
    """
    Method that loads all sound effects at application start.
    Loads into sounds dictionary.
    Tuple unpacking is used to get and assign both the name and path of each sound.
    
    Args:
        parent (QObject | None): The parent QObject for the QSoundEffect instances.
        
    Returns:
        None
    """
    sounds = {
        "QWERTY": "qwerty.wav",
        "AZERTY": "azerty.wav",
        "DVORAK": "dvorak.wav",
        "COLEMAK": "colemak.wav",
    }

    for name, path in sounds.items():
        full_path = (SOUNDS_PATH / path).resolve()
        eff = QSoundEffect(parent)
        eff.setSource(QUrl.fromLocalFile(str(full_path)))
        eff.setVolume(0.5)



#def set_keyboard_sound(sound_effect):
#implementation of sound effect when keyboard layout is changed

