from enum import unique, Enum, auto

FRAME_RATE = 50


@unique
class EventType(Enum):
    Keypress = auto()
    MouseMove = auto()
    MouseClick = auto()
