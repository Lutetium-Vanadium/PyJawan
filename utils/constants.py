from enum import unique, Enum, auto

FRAME_RATE = 50


@unique
class EventType(Enum):
    KeyUp = auto()
    KeyDown = auto()
    MouseMove = auto()
    MouseClick = auto()


@unique
class HorizontalAlignment(Enum):
    Left = auto()
    Right = auto()
    Center = auto()


@unique
class VerticalAlignment(Enum):
    Top = auto()
    Center = auto()
    Bottom = auto()
