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



def set_keyboard_sound(name: str):
    """Set CURRENT_SOUND from a string (case-insensitive). Preview it if valid."""
    global CURRENT_SOUND
    if not name:  # empty string
        return
    candidate = SOUNDS.get(name.lower())
    if candidate is None:
        # Not a sound option; ignore gracefully.
        print(f"No sound mapped for '{name}'")
        CURRENT_SOUND = None
        return
    CURRENT_SOUND = candidate
    
    CURRENT_SOUND.stop()
    CURRENT_SOUND.play()

def play_current_sound():
    """Play the currently selected sound if any."""
    if CURRENT_SOUND is not None:
        CURRENT_SOUND.stop()  # helps avoid overlap
        CURRENT_SOUND.play()