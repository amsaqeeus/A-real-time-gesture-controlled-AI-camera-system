"""
timer.py

High precision timer utilities.
"""

from __future__ import annotations

import time


class Timer:
    """
    Simple high precision timer.
    """

    def __init__(self) -> None:

        self.reset()

    # ---------------------------------------------------------

    def reset(self) -> None:

        self._start = time.perf_counter()

    # ---------------------------------------------------------

    @property
    def elapsed(self) -> float:

        return time.perf_counter() - self._start

    # ---------------------------------------------------------

    def has_elapsed(
        self,
        seconds: float,
    ) -> bool:

        return self.elapsed >= seconds