from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl, QObject
from pathlib import Path

SOUNDS: dict[str, QSoundEffect] = {}
CURRENT_SOUND: QSoundEffect | None = None
SOUNDS_PATH = Path("./assets/sounds/")

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
    
    print("Loading sound effect...")
    
    sounds = {
        "GAME": "game.wav",
        "POP": "pop.wav",
    }

    for name, path in sounds.items():
        full_path = (SOUNDS_PATH / path).resolve()
        eff = QSoundEffect(parent)
        eff.setSource(QUrl.fromLocalFile(str(full_path)))
        eff.setVolume(0.5)
        
        SOUNDS[name.lower()] = eff    



def set_keyboard_sound(sound_effect):
    global CURRENT_SOUND
    CURRENT_SOUND = SOUNDS.get(sound_effect.lower())
    
    CURRENT_SOUND.play()
