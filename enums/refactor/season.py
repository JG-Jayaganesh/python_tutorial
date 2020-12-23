from enum import Enum, auto


class Season(Enum):
    SUMMER = auto()
    WINTER = auto()
    SPRING = auto()
    FALL = auto()


class Dummy(Enum):
    OTHER = auto()
