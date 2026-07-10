"""
landmark.py

Data models representing hand landmarks.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Tuple


@dataclass(slots=True)
class Landmark:
    """
    Represents a single 3D hand landmark.
    """

    id: int
    x: float
    y: float
    z: float

    def as_tuple(self) -> Tuple[float, float, float]:
        return (
            self.x,
            self.y,
            self.z,
        )

    def to_pixel(
        self,
        frame_width: int,
        frame_height: int,
    ) -> Tuple[int, int]:
        """
        Convert normalized coordinates to pixel coordinates.
        """

        return (
            int(self.x * frame_width),
            int(self.y * frame_height),
        )

    def distance_to(
        self,
        other: "Landmark",
    ) -> float:
        """
        Euclidean distance between two landmarks.
        """

        return sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.z - other.z) ** 2
        )

    def copy(self) -> "Landmark":
        """
        Return a copy of this landmark.
        """

        return Landmark(
            id=self.id,
            x=self.x,
            y=self.y,
            z=self.z,
        )

    @property
    def xy(self) -> Tuple[float, float]:
        return (
            self.x,
            self.y,
        )

    @property
    def xyz(self) -> Tuple[float, float, float]:
        return (
            self.x,
            self.y,
            self.z,
        )