"""
countdown.py

Countdown manager for GestureCam.
"""

from __future__ import annotations

import time


class Countdown:
    """
    Handles countdown timing.
    """

    def __init__(
        self,
        duration: int = 3,
    ) -> None:

        self.duration = duration

        self._start_time: float | None = None

        self._running = False

    # ---------------------------------------------------------

    def start(self) -> None:

        if self._running:
            return

        self._start_time = time.perf_counter()

        self._running = True

    # ---------------------------------------------------------

    def cancel(self) -> None:

        self._running = False

        self._start_time = None

    # ---------------------------------------------------------

    @property
    def running(self) -> bool:

        return self._running

    # ---------------------------------------------------------

    @property
    def finished(self) -> bool:

        if not self._running:
            return False

        return self.remaining <= 0

    # ---------------------------------------------------------

    @property
    def remaining(self) -> int:

        if not self._running:
            return self.duration

        elapsed = time.perf_counter() - self._start_time

        remaining = self.duration - int(elapsed)

        return max(
            remaining,
            0,
        )

    # ---------------------------------------------------------

    @property
    def progress(self) -> float:

        if not self._running:
            return 0.0

        elapsed = time.perf_counter() - self._start_time

        return min(
            elapsed / self.duration,
            1.0,
        )

    # ---------------------------------------------------------

    def update(self) -> bool:
        """
        Returns True exactly once when the countdown finishes.
        """

        if not self._running:
            return False

        if self.finished:

            self.cancel()

            return True

        return False