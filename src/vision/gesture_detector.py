"""
gesture_detector.py

Gesture recognition engine.
"""

from __future__ import annotations

from typing import List

from .gestures import Gesture
from .hand import Hand
from src.utils.geometry import Geometry


class GestureDetector:

    THUMB_TIP = 4

    INDEX_TIP = 8
    MIDDLE_TIP = 12
    RING_TIP = 16
    PINKY_TIP = 20

    INDEX_PIP = 6
    MIDDLE_PIP = 10
    RING_PIP = 14
    PINKY_PIP = 18

    # ---------------------------------------------------------

    def detect(
        self,
        hands: List[Hand],
    ) -> Gesture:

        if not hands:
            return Gesture.UNKNOWN

        if len(hands) == 2:

            gesture = self.detect_frame(hands)

            if gesture != Gesture.UNKNOWN:
                return gesture

        hand = hands[0]

        for detector in (
            self.detect_pinch,
            self.detect_thumbs_up,
            self.detect_peace,
            self.detect_open_hand,
            self.detect_fist,
        ):

            gesture = detector(hand)

            if gesture != Gesture.UNKNOWN:
                return gesture

        return Gesture.UNKNOWN

    # ---------------------------------------------------------

    def detect_fist(
        self,
        hand: Hand,
    ) -> Gesture:

        if self._finger_states(hand) == [
            False,
            False,
            False,
            False,
        ]:
            return Gesture.FIST

        return Gesture.UNKNOWN

    # ---------------------------------------------------------

    def detect_open_hand(
        self,
        hand: Hand,
    ) -> Gesture:

        if self._finger_states(hand) == [
            True,
            True,
            True,
            True,
        ]:
            return Gesture.OPEN_HAND

        return Gesture.UNKNOWN

    # ---------------------------------------------------------

    def detect_peace(
        self,
        hand: Hand,
    ) -> Gesture:

        if self._finger_states(hand) == [
            True,
            True,
            False,
            False,
        ]:
            return Gesture.PEACE

        return Gesture.UNKNOWN

    # ---------------------------------------------------------

    def detect_thumbs_up(
        self,
        hand: Hand,
    ) -> Gesture:

        fingers = self._finger_states(hand)

        if (
            hand.thumb_tip.y < hand.wrist.y
            and fingers == [
                False,
                False,
                False,
                False,
            ]
        ):
            return Gesture.THUMBS_UP

        return Gesture.UNKNOWN

    # ---------------------------------------------------------

    def detect_pinch(
        self,
        hand: Hand,
    ) -> Gesture:

        if Geometry.is_close(
            hand.thumb_tip,
            hand.index_tip,
            hand,
            threshold=0.12,
        ):
            return Gesture.PINCH

        return Gesture.UNKNOWN

    # ---------------------------------------------------------

    def detect_frame(
        self,
        hands: List[Hand],
    ) -> Gesture:

        if len(hands) != 2:
            return Gesture.UNKNOWN

        left = next(
            (hand for hand in hands if hand.is_left),
            None,
        )

        right = next(
            (hand for hand in hands if hand.is_right),
            None,
        )

        if left is None or right is None:
            return Gesture.UNKNOWN

        thumb_distance = Geometry.distance(
            left.thumb_tip,
            right.thumb_tip,
        )

        index_distance = Geometry.distance(
            left.index_tip,
            right.index_tip,
        )

        if (
            thumb_distance > 0.20
            and index_distance > 0.20
        ):
            return Gesture.FRAME

        return Gesture.UNKNOWN

    # ---------------------------------------------------------

    def _finger_states(
        self,
        hand: Hand,
    ) -> List[bool]:

        return [

            hand.index_tip.y
            < hand.get(self.INDEX_PIP).y,

            hand.middle_tip.y
            < hand.get(self.MIDDLE_PIP).y,

            hand.ring_tip.y
            < hand.get(self.RING_PIP).y,

            hand.pinky_tip.y
            < hand.get(self.PINKY_PIP).y,

        ]