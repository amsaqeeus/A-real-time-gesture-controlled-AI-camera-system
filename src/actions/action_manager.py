"""
action_manager.py

Maps gestures to application actions.
"""

from __future__ import annotations

from src.actions.actions import Action
from src.vision.gestures import Gesture

class ActionManager:
    """Maps gestures to actions."""

    def __init__(self) -> None:

        self._last_gesture = Gesture.UNKNOWN

    # ---------------------------------------------------------

    def update(
        self,
        gesture: Gesture,
    ) -> Action:

        if gesture == self._last_gesture:
            return Action.NONE

        self._last_gesture = gesture

        mapping = {

            Gesture.UNKNOWN: Action.NONE,

            Gesture.OPEN_HAND: Action.READY,

            Gesture.FRAME: Action.START_COUNTDOWN,

            Gesture.THUMBS_UP: Action.CAPTURE,

            Gesture.PEACE: Action.SAVE,

            Gesture.FIST: Action.CANCEL,

            Gesture.PINCH: Action.FOCUS,

        }

        return mapping.get(
            gesture,
            Action.NONE,
        )

    # ---------------------------------------------------------

    def reset(self) -> None:

        self._last_gesture = Gesture.UNKNOWN

    # ---------------------------------------------------------

    @property
    def last_gesture(self) -> Gesture:

        return self._last_gesture