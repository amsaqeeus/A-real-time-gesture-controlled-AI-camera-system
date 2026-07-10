"""
actions.py

Application actions.
"""

from enum import Enum, auto


class Action(Enum):
    NONE = auto()

    READY = auto()

    START_COUNTDOWN = auto()

    CAPTURE = auto()

    SAVE = auto()

    CANCEL = auto()

    FOCUS = auto()