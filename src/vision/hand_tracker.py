# """
# hand_tracker.py

# Professional MediaPipe hand tracking module.
# """

# from __future__ import annotations

# from typing import List, Optional

# import cv2
# import mediapipe as mp
# import numpy as np

# from config.settings import (
#     MAX_NUM_HANDS,
#     MIN_DETECTION_CONFIDENCE,
#     MIN_TRACKING_CONFIDENCE,
# )

# from .hand import Hand
# from .landmark import Landmark


# class HandTracker:
#     """Detect and draw hands using MediaPipe."""

#     def __init__(
#         self,
#         max_num_hands: int = MAX_NUM_HANDS,
#         min_detection_confidence: float = MIN_DETECTION_CONFIDENCE,
#         min_tracking_confidence: float = MIN_TRACKING_CONFIDENCE,
#     ) -> None:

#         self._mp_hands = mp.solutions.hands
#         self._drawer = mp.solutions.drawing_utils
#         self._styles = mp.solutions.drawing_styles

#         self._detector = self._mp_hands.Hands(
#             static_image_mode=False,
#             model_complexity=1,
#             max_num_hands=max_num_hands,
#             min_detection_confidence=min_detection_confidence,
#             min_tracking_confidence=min_tracking_confidence,
#         )

#         self._results = None

#     # -------------------------------------------------------------

#     def detect(self, frame: np.ndarray) -> List[Hand]:
#         """
#         Detect hands inside a BGR frame.
#         """

#         rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         rgb.flags.writeable = False

#         self._results = self._detector.process(rgb)

#         rgb.flags.writeable = True

#         if (
#             self._results.multi_hand_landmarks is None
#             or self._results.multi_handedness is None
#         ):
#             return []

#         hands: List[Hand] = []

#         for landmarks, handedness in zip(
#             self._results.multi_hand_landmarks,
#             self._results.multi_handedness,
#         ):

#             hand = Hand(
#                 label=handedness.classification[0].label,
#                 confidence=handedness.classification[0].score,
#                 landmarks=[
#                     Landmark(
#                         id=index,
#                         x=landmark.x,
#                         y=landmark.y,
#                         z=landmark.z,
#                     )
#                     for index, landmark in enumerate(
#                         landmarks.landmark
#                     )
#                 ],
#             )

#             hands.append(hand)

#         return hands

#     # -------------------------------------------------------------

#     def draw(self, frame: np.ndarray) -> np.ndarray:
#         """
#         Draw the latest detected hands.
#         """

#         if self._results is None:
#             return frame

#         if self._results.multi_hand_landmarks is None:
#             return frame

#         for hand_landmarks in self._results.multi_hand_landmarks:

#             self._drawer.draw_landmarks(
#                 frame,
#                 hand_landmarks,
#                 self._mp_hands.HAND_CONNECTIONS,
#                 self._styles.get_default_hand_landmarks_style(),
#                 self._styles.get_default_hand_connections_style(),
#             )

#         return frame

#     # -------------------------------------------------------------

#     def clear(self) -> None:

#         self._results = None

#     # -------------------------------------------------------------

#     @property
#     def results(self):

#         return self._results

#     # -------------------------------------------------------------

#     def close(self) -> None:

#         self._detector.close()

#     # -------------------------------------------------------------

#     def __enter__(self):

#         return self

#     # -------------------------------------------------------------

#     def __exit__(
#         self,
#         exc_type,
#         exc_val,
#         exc_tb,
#     ):

#         self.close()

"""
hand_tracker.py

Professional MediaPipe hand tracking module.
"""

from __future__ import annotations

from typing import List, Optional, Tuple

import cv2
import mediapipe as mp
import numpy as np

from config.settings import (
    MAX_NUM_HANDS,
    MIN_DETECTION_CONFIDENCE,
    MIN_TRACKING_CONFIDENCE,
)

from .hand import Hand
from .landmark import Landmark


class HandTracker:
    """Detect and draw hands using MediaPipe."""

    def __init__(
        self,
        max_num_hands: int = MAX_NUM_HANDS,
        min_detection_confidence: float = MIN_DETECTION_CONFIDENCE,
        min_tracking_confidence: float = MIN_TRACKING_CONFIDENCE,
    ) -> None:

        self._mp_hands = mp.solutions.hands
        self._drawer = mp.solutions.drawing_utils
        self._styles = mp.solutions.drawing_styles

        self._detector = self._mp_hands.Hands(
            static_image_mode=False,
            model_complexity=1,
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

        self._results = None

    # -------------------------------------------------------------

    def detect(self, frame: np.ndarray) -> List[Hand]:

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        rgb.flags.writeable = False

        self._results = self._detector.process(rgb)

        rgb.flags.writeable = True

        if (
            self._results.multi_hand_landmarks is None
            or self._results.multi_handedness is None
        ):
            return []

        hands: List[Hand] = []

        for landmarks, handedness in zip(
            self._results.multi_hand_landmarks,
            self._results.multi_handedness,
        ):

            hand = Hand(
                label=handedness.classification[0].label,
                confidence=handedness.classification[0].score,
                landmarks=[
                    Landmark(
                        id=index,
                        x=landmark.x,
                        y=landmark.y,
                        z=landmark.z,
                    )
                    for index, landmark in enumerate(
                        landmarks.landmark
                    )
                ],
            )

            hands.append(hand)

        return hands

    # -------------------------------------------------------------

    def draw(self, frame: np.ndarray) -> np.ndarray:

        if self._results is None:
            return frame

        if self._results.multi_hand_landmarks is None:
            return frame

        for hand_landmarks in self._results.multi_hand_landmarks:

            self._drawer.draw_landmarks(
                frame,
                hand_landmarks,
                self._mp_hands.HAND_CONNECTIONS,
                self._styles.get_default_hand_landmarks_style(),
                self._styles.get_default_hand_connections_style(),
            )

        return frame

    # -------------------------------------------------------------
    # NEW METHODS
    # -------------------------------------------------------------

    @staticmethod
    def landmark_pixel(
        hand: Hand,
        landmark_id: int,
        frame_shape: tuple[int, int, int],
    ) -> Tuple[int, int]:

        h, w = frame_shape[:2]

        point = hand.get(landmark_id)

        return (
            int(point.x * w),
            int(point.y * h),
        )

    # -------------------------------------------------------------

    def get_thumb_tip(
        self,
        hand: Hand,
        frame_shape,
    ) -> Tuple[int, int]:

        return self.landmark_pixel(
            hand,
            4,
            frame_shape,
        )

    # -------------------------------------------------------------

    def get_index_tip(
        self,
        hand: Hand,
        frame_shape,
    ) -> Tuple[int, int]:

        return self.landmark_pixel(
            hand,
            8,
            frame_shape,
        )

    # -------------------------------------------------------------

    def get_middle_tip(
        self,
        hand: Hand,
        frame_shape,
    ) -> Tuple[int, int]:

        return self.landmark_pixel(
            hand,
            12,
            frame_shape,
        )

    # -------------------------------------------------------------

    def get_ring_tip(
        self,
        hand: Hand,
        frame_shape,
    ) -> Tuple[int, int]:

        return self.landmark_pixel(
            hand,
            16,
            frame_shape,
        )

    # -------------------------------------------------------------

    def get_pinky_tip(
        self,
        hand: Hand,
        frame_shape,
    ) -> Tuple[int, int]:

        return self.landmark_pixel(
            hand,
            20,
            frame_shape,
        )

    # -------------------------------------------------------------

    def get_hand_center(
        self,
        hand: Hand,
        frame_shape,
    ) -> Tuple[int, int]:

        h, w = frame_shape[:2]

        xs = [lm.x for lm in hand.landmarks]
        ys = [lm.y for lm in hand.landmarks]

        return (
            int(sum(xs) / len(xs) * w),
            int(sum(ys) / len(ys) * h),
        )

    # -------------------------------------------------------------

    def get_all_landmarks(
        self,
        hand: Hand,
        frame_shape,
    ) -> List[Tuple[int, int]]:

        h, w = frame_shape[:2]

        return [
            (
                int(lm.x * w),
                int(lm.y * h),
            )
            for lm in hand.landmarks
        ]

    # -------------------------------------------------------------

    def clear(self) -> None:

        self._results = None

    # -------------------------------------------------------------

    @property
    def results(self):

        return self._results

    # -------------------------------------------------------------

    def close(self) -> None:

        self._detector.close()

    # -------------------------------------------------------------

    def __enter__(self):

        return self

    # -------------------------------------------------------------

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ):

        self.close()