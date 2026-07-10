"""
window.py

Application window management.
"""

from __future__ import annotations

import cv2

from config.settings import WINDOW_NAME


class Window:
    """
    Handles the application window.
    """

    def __init__(
        self,
        title: str = WINDOW_NAME,
    ) -> None:

        self.title = title

        cv2.namedWindow(
            self.title,
            cv2.WINDOW_NORMAL,
        )

    # ---------------------------------------------------------

    def show(
        self,
        frame,
    ) -> None:

        cv2.imshow(
            self.title,
            frame,
        )

    # ---------------------------------------------------------

    @staticmethod
    def key() -> int:

        return cv2.waitKey(1) & 0xFF

    # ---------------------------------------------------------

    @staticmethod
    def should_close(
        key: int,
    ) -> bool:

        return key in (
            27,         # ESC
            ord("q"),
            ord("Q"),
        )

    # ---------------------------------------------------------

    def destroy(self) -> None:

        cv2.destroyWindow(
            self.title,
        )