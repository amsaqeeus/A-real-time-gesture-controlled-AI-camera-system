"""
fps.py

FPS calculator.
"""

from __future__ import annotations

import time


class FPSCounter:

    def __init__(self) -> None:

        self._previous = time.perf_counter()

        self._fps = 0.0

    # ---------------------------------------------------------

    def update(self) -> float:

        current = time.perf_counter()

        delta = current - self._previous

        self._previous = current

        if delta > 0:

            self._fps = 1.0 / delta

        return self._fps

    # ---------------------------------------------------------

    @property
    def fps(self) -> float:

        return self._fps