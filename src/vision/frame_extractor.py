"""
frame_extractor.py

Builds and manages the virtual camera frame
created by two hands.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import cv2
import numpy as np

from .hand import Hand


@dataclass
class CaptureFrame:

    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def width(self):

        return self.x2 - self.x1

    @property
    def height(self):

        return self.y2 - self.y1

    @property
    def valid(self):

        return self.width > 60 and self.height > 60


class FrameExtractor:

    """
    Creates the capture rectangle
    from two detected hands.
    """

    LEFT_INDEX = 8
    LEFT_THUMB = 4

    RIGHT_INDEX = 8
    RIGHT_THUMB = 4

    def __init__(self):

        self.last_frame: Optional[CaptureFrame] = None

    # -------------------------------------------------------------

    def get_capture_frame(
        self,
        hands: list[Hand],
        frame: np.ndarray,
    ) -> Optional[CaptureFrame]:

        if len(hands) != 2:
            return None

        h, w = frame.shape[:2]

        left = None
        right = None

        for hand in hands:

            if hand.label.lower() == "left":
                left = hand

            elif hand.label.lower() == "right":
                right = hand

        if left is None or right is None:
            return None

        left_index = left.get(self.LEFT_INDEX)
        left_thumb = left.get(self.LEFT_THUMB)

        right_index = right.get(self.RIGHT_INDEX)
        right_thumb = right.get(self.RIGHT_THUMB)

        x1 = int(left_thumb.x * w)
        y1 = int(left_index.y * h)

        x2 = int(right_thumb.x * w)
        y2 = int(right_index.y * h)

        if x1 > x2:
            x1, x2 = x2, x1

        if y1 > y2:
            y1, y2 = y2, y1

        margin = 15

        capture = CaptureFrame(

            max(0, x1 - margin),

            max(0, y1 - margin),

            min(w, x2 + margin),

            min(h, y2 + margin),

        )

        self.last_frame = capture

        return capture

    # -------------------------------------------------------------

    def crop(

        self,

        frame: np.ndarray,

        capture: CaptureFrame,

    ) -> np.ndarray:

        return frame[
            capture.y1:capture.y2,
            capture.x1:capture.x2,
        ].copy()

    # -------------------------------------------------------------

    def draw(

        self,

        frame: np.ndarray,

        capture: Optional[CaptureFrame],

    ) -> np.ndarray:

        if capture is None:
            return frame

        color = (0, 255, 0)

        cv2.rectangle(

            frame,

            (capture.x1, capture.y1),

            (capture.x2, capture.y2),

            color,

            3,

        )

        return frame