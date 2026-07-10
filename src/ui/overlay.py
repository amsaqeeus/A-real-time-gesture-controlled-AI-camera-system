# """
# overlay.py

# Drawing utilities for GestureCam.
# """

# from __future__ import annotations

# import cv2
# import numpy as np

# from src.ui.colors import Color

# class Overlay:
#     """Draws information on the camera frame."""

#     FONT = cv2.FONT_HERSHEY_SIMPLEX

#     # ---------------------------------------------------------

#     @staticmethod
#     def draw_title(
#         frame: np.ndarray,
#         text: str = "GestureCam",
#     ) -> np.ndarray:

#         cv2.putText(
#             frame,
#             text,
#             (20, 40),
#             Overlay.FONT,
#             1.0,
#             Color.CYAN,
#             2,
#             cv2.LINE_AA,
#         )

#         return frame

#     # ---------------------------------------------------------

#     @staticmethod
#     def draw_gesture(
#         frame: np.ndarray,
#         gesture: str,
#     ) -> np.ndarray:

#         cv2.putText(
#             frame,
#             f"Gesture : {gesture}",
#             (20, 80),
#             Overlay.FONT,
#             0.8,
#             Color.GREEN,
#             2,
#             cv2.LINE_AA,
#         )

#         return frame

#     # ---------------------------------------------------------

#     @staticmethod
#     def draw_status(
#         frame: np.ndarray,
#         status: str,
#     ) -> np.ndarray:

#         cv2.putText(
#             frame,
#             f"Status : {status}",
#             (20, 120),
#             Overlay.FONT,
#             0.8,
#             Color.ORANGE,
#             2,
#             cv2.LINE_AA,
#         )

#         return frame

#     # ---------------------------------------------------------

#     @staticmethod
#     def draw_fps(
#         frame: np.ndarray,
#         fps: float,
#     ) -> np.ndarray:

#         cv2.putText(
#             frame,
#             f"FPS : {fps:.1f}",
#             (20, 160),
#             Overlay.FONT,
#             0.8,
#             Color.WHITE,
#             2,
#             cv2.LINE_AA,
#         )

#         return frame

#     # ---------------------------------------------------------

#     @staticmethod
#     def draw_countdown(
#         frame: np.ndarray,
#         value: int,
#     ) -> np.ndarray:

#         if value <= 0:
#             return frame

#         h, w = frame.shape[:2]

#         text = str(value)

#         (tw, th), _ = cv2.getTextSize(
#             text,
#             Overlay.FONT,
#             4,
#             6,
#         )

#         x = (w - tw) // 2
#         y = (h + th) // 2

#         cv2.putText(
#             frame,
#             text,
#             (x, y),
#             Overlay.FONT,
#             4,
#             Color.RED,
#             6,
#             cv2.LINE_AA,
#         )

#         return frame

#     # ---------------------------------------------------------

#     @staticmethod
#     def flash(
#         frame: np.ndarray,
#         alpha: float = 0.6,
#     ) -> np.ndarray:

#         white = np.full_like(
#             frame,
#             255,
#         )

#         return cv2.addWeighted(
#             white,
#             alpha,
#             frame,
#             1 - alpha,
#             0,
#         )

#     # ---------------------------------------------------------

#     @staticmethod
#     def draw_saved(
#         frame: np.ndarray,
#     ) -> np.ndarray:

#         cv2.putText(
#             frame,
#             "Photo Saved!",
#             (20, 200),
#             Overlay.FONT,
#             0.9,
#             Color.GREEN,
#             3,
#             cv2.LINE_AA,
#         )

#         return frame

#     # ---------------------------------------------------------

#     @staticmethod
#     def draw_crosshair(
#         frame: np.ndarray,
#     ) -> np.ndarray:

#         h, w = frame.shape[:2]

#         cx = w // 2
#         cy = h // 2

#         cv2.line(
#             frame,
#             (cx - 20, cy),
#             (cx + 20, cy),
#             Color.GRAY,
#             2,
#         )

#         cv2.line(
#             frame,
#             (cx, cy - 20),
#             (cx, cy + 20),
#             Color.GRAY,
#             2,
#         )

#         return frame
    
"""
overlay.py

Drawing utilities for GestureCam.
"""

from __future__ import annotations

import cv2
import numpy as np

from src.ui.colors import Color


class Overlay:
    """Draws information on the camera frame."""

    FONT = cv2.FONT_HERSHEY_SIMPLEX

    # ---------------------------------------------------------

    @staticmethod
    def draw_title(
        frame: np.ndarray,
        text: str = "GestureCam",
    ) -> np.ndarray:

        cv2.putText(
            frame,
            text,
            (20, 40),
            Overlay.FONT,
            1.0,
            Color.CYAN,
            2,
            cv2.LINE_AA,
        )

        return frame

    # ---------------------------------------------------------

    @staticmethod
    def draw_gesture(
        frame: np.ndarray,
        gesture: str,
    ) -> np.ndarray:

        cv2.putText(
            frame,
            f"Gesture : {gesture}",
            (20, 80),
            Overlay.FONT,
            0.8,
            Color.GREEN,
            2,
            cv2.LINE_AA,
        )

        return frame

    # ---------------------------------------------------------

    @staticmethod
    def draw_status(
        frame: np.ndarray,
        status: str,
    ) -> np.ndarray:

        cv2.putText(
            frame,
            f"Status : {status}",
            (20, 120),
            Overlay.FONT,
            0.8,
            Color.ORANGE,
            2,
            cv2.LINE_AA,
        )

        return frame

    # ---------------------------------------------------------

    @staticmethod
    def draw_fps(
        frame: np.ndarray,
        fps: float,
    ) -> np.ndarray:

        cv2.putText(
            frame,
            f"FPS : {fps:.1f}",
            (20, 160),
            Overlay.FONT,
            0.8,
            Color.WHITE,
            2,
            cv2.LINE_AA,
        )

        return frame

    # ---------------------------------------------------------

    @staticmethod
    def draw_countdown(
        frame: np.ndarray,
        value: int,
    ) -> np.ndarray:

        if value <= 0:
            return frame

        h, w = frame.shape[:2]

        text = str(value)

        (tw, th), _ = cv2.getTextSize(
            text,
            Overlay.FONT,
            4,
            6,
        )

        x = (w - tw) // 2
        y = (h + th) // 2

        cv2.putText(
            frame,
            text,
            (x, y),
            Overlay.FONT,
            4,
            Color.RED,
            6,
            cv2.LINE_AA,
        )

        return frame

    # ---------------------------------------------------------

    @staticmethod
    def draw_capture_frame(
        frame: np.ndarray,
        capture,
    ) -> np.ndarray:
        """
        Draw the virtual camera frame.
        """

        if capture is None:
            return frame

        cv2.rectangle(
            frame,
            (capture.x1, capture.y1),
            (capture.x2, capture.y2),
            Color.GREEN,
            3,
        )

        cv2.putText(
            frame,
            "Capture Area",
            (capture.x1, capture.y1 - 10),
            Overlay.FONT,
            0.7,
            Color.GREEN,
            2,
            cv2.LINE_AA,
        )

        return frame

    # ---------------------------------------------------------

    @staticmethod
    def flash(
        frame: np.ndarray,
        alpha: float = 0.6,
    ) -> np.ndarray:

        white = np.full_like(frame, 255)

        return cv2.addWeighted(
            white,
            alpha,
            frame,
            1 - alpha,
            0,
        )

    # ---------------------------------------------------------

    @staticmethod
    def draw_saved(
        frame: np.ndarray,
    ) -> np.ndarray:

        cv2.putText(
            frame,
            "Photo Saved!",
            (20, 200),
            Overlay.FONT,
            0.9,
            Color.GREEN,
            3,
            cv2.LINE_AA,
        )

        return frame

    # ---------------------------------------------------------

    @staticmethod
    def draw_crosshair(
        frame: np.ndarray,
    ) -> np.ndarray:

        h, w = frame.shape[:2]

        cx = w // 2
        cy = h // 2

        cv2.line(
            frame,
            (cx - 20, cy),
            (cx + 20, cy),
            Color.GRAY,
            2,
        )

        cv2.line(
            frame,
            (cx, cy - 20),
            (cx, cy + 20),
            Color.GRAY,
            2,
        )

        return frame