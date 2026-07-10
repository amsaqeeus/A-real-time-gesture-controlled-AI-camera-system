"""
frame_processor.py

Frame processing utilities for GestureCam.
"""

from __future__ import annotations

import time

import cv2
import numpy as np


class FrameProcessor:
    """
    Handles all preprocessing operations applied
    to each webcam frame before further processing.
    """

    def __init__(
        self,
        mirror: bool = True,
        brightness: float = 1.0,
        contrast: float = 1.0,
    ) -> None:

        self.mirror = mirror
        self.brightness = brightness
        self.contrast = contrast

        self._previous_time = time.perf_counter()
        self._fps = 0.0

    # ---------------------------------------------------------

    def process(self, frame: np.ndarray) -> np.ndarray:
        """
        Complete preprocessing pipeline.
        """

        frame = self.flip(frame)
        frame = self.adjust(frame)

        frame = self.beauty_filter(frame)


        return frame

    # ---------------------------------------------------------

    def flip(self, frame: np.ndarray) -> np.ndarray:
        """
        Mirror the webcam image.
        """

        if self.mirror:
            return cv2.flip(frame, 1)

        return frame

    # ---------------------------------------------------------

    def adjust(self, frame: np.ndarray) -> np.ndarray:
        """
        Apply brightness and contrast.
        """

        return cv2.convertScaleAbs(
            frame,
            alpha=self.contrast,
            beta=(self.brightness - 1.0) * 50,
        )

    # ---------------------------------------------------------

    @staticmethod
    def bgr_to_rgb(frame: np.ndarray) -> np.ndarray:

        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # ---------------------------------------------------------

    @staticmethod
    def rgb_to_bgr(frame: np.ndarray) -> np.ndarray:

        return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # ---------------------------------------------------------

    @staticmethod
    def resize(
        frame: np.ndarray,
        width: int,
        height: int,
    ) -> np.ndarray:

        return cv2.resize(
            frame,
            (width, height),
            interpolation=cv2.INTER_AREA,
        )

    # ---------------------------------------------------------
        # ---------------------------------------------------------

    @staticmethod
    def beauty_filter(
        frame: np.ndarray,
    ) -> np.ndarray:
        """
        Apply a soft beauty filter.
        """

        # Skin smoothing
        smooth = cv2.bilateralFilter(
            frame,
            d=9,
            sigmaColor=75,
            sigmaSpace=75,
        )

        # Blend original and smoothed image
        frame = cv2.addWeighted(
            frame,
            0.4,
            smooth,
            0.6,
            0,
        )

        # Slight brightness
        frame = cv2.convertScaleAbs(
            frame,
            alpha=1.08,
            beta=8,
        )

        # Slight color boost
        hsv = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2HSV,
        )

        hsv[:, :, 1] = np.clip(
            hsv[:, :, 1] * 1.08,
            0,
            255,
        ).astype(np.uint8)

        frame = cv2.cvtColor(
            hsv,
            cv2.COLOR_HSV2BGR,
        )

        return frame
    
    def update_fps(self) -> float:
        """
        Calculate current FPS.
        """

        current_time = time.perf_counter()

        delta = current_time - self._previous_time

        self._previous_time = current_time

        if delta > 0:
            self._fps = 1.0 / delta

        return self._fps

    # ---------------------------------------------------------

    @property
    def fps(self) -> float:

        return self._fps

    # ---------------------------------------------------------

    @staticmethod
    def blur(frame: np.ndarray) -> np.ndarray:

        return cv2.GaussianBlur(
            frame,
            (5, 5),
            0,
        )

    # ---------------------------------------------------------

    @staticmethod
    def sharpen(frame: np.ndarray) -> np.ndarray:

        kernel = np.array(
            [
                [0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0],
            ]
        )

        return cv2.filter2D(
            frame,
            -1,
            kernel,
        )

    # ---------------------------------------------------------

    @staticmethod
    def grayscale(frame: np.ndarray) -> np.ndarray:

        return cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY,
        )

    # ---------------------------------------------------------

    @staticmethod
    def draw_fps(
        frame: np.ndarray,
        fps: float,
    ) -> np.ndarray:

        cv2.putText(
            frame,
            f"FPS: {fps:.1f}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

        return frame