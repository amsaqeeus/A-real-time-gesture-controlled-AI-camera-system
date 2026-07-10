"""
camera_manager.py

Professional webcam manager for GestureCam.
"""

from __future__ import annotations

from typing import Optional

import cv2
import numpy as np

from config.settings import (
    CAMERA_INDEX,
    FRAME_HEIGHT,
    FRAME_WIDTH,
)


class CameraError(Exception):
    """Raised when the camera cannot be accessed."""


class CameraManager:
    """
    Handles webcam initialization, frame acquisition,
    configuration and cleanup.
    """

    def __init__(
        self,
        camera_index: int = CAMERA_INDEX,
        width: int = FRAME_WIDTH,
        height: int = FRAME_HEIGHT,
    ) -> None:

        self.camera_index = camera_index
        self.width = width
        self.height = height

        self._capture: Optional[cv2.VideoCapture] = None

    # ---------------------------------------------------------

    def open(self) -> None:
        """Open the webcam."""

        if self.is_opened:
            return

        self._capture = cv2.VideoCapture(self.camera_index)

        if not self._capture.isOpened():
            raise CameraError(
                f"Unable to open camera {self.camera_index}"
            )

        self._capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self._capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

    # ---------------------------------------------------------

    def read(self) -> np.ndarray:
        """
        Read a frame from the webcam.

        Returns
        -------
        numpy.ndarray
            Current camera frame.

        Raises
        ------
        CameraError
            If frame cannot be read.
        """

        if self._capture is None:
            raise CameraError("Camera has not been opened.")

        success, frame = self._capture.read()

        if not success:
            raise CameraError("Failed to read frame.")

        return frame

    # ---------------------------------------------------------

    def release(self) -> None:
        """Release webcam resources."""

        if self._capture is not None:

            self._capture.release()

            self._capture = None

        cv2.destroyAllWindows()

    # ---------------------------------------------------------

    @property
    def is_opened(self) -> bool:
        """Return True if camera is opened."""

        return (
            self._capture is not None
            and self._capture.isOpened()
        )

    # ---------------------------------------------------------

    @property
    def fps(self) -> float:
        """Return camera FPS."""

        if self._capture is None:
            return 0.0

        return float(
            self._capture.get(cv2.CAP_PROP_FPS)
        )

    # ---------------------------------------------------------

    @property
    def frame_width(self) -> int:

        if self._capture is None:
            return self.width

        return int(
            self._capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        )

    # ---------------------------------------------------------

    @property
    def frame_height(self) -> int:

        if self._capture is None:
            return self.height

        return int(
            self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )

    # ---------------------------------------------------------

    def __enter__(self) -> "CameraManager":

        self.open()

        return self

    # ---------------------------------------------------------

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ) -> None:

        self.release()