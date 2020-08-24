from enum import unique, Enum, auto

FRAME_RATE = 50


@unique
class EventType(Enum):
    KeyUp = auto()
    KeyDown = auto()
    MouseMove = auto()
    MouseClick = auto()
