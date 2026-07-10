"""
gestures.py

Gesture definitions for GestureCam.
"""

from enum import Enum, auto


class Gesture(Enum):
    UNKNOWN = auto()

    FIST = auto()

    OPEN_HAND = auto()

    THUMBS_UP = auto()

    THUMBS_DOWN = auto()

    PEACE = auto()

    OK = auto()

    PINCH = auto()

    FRAME = auto()

    HEART = auto()