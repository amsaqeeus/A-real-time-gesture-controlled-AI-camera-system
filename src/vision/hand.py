"""
hand.py

Hand data model used throughout GestureCam.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from .landmark import Landmark


@dataclass(slots=True)
class Hand:
    """
    Represents one detected hand.
    """

    label: str
    confidence: float
    landmarks: List[Landmark] = field(default_factory=list)

    # ------------------------------------------------------------------

    def __len__(self) -> int:
        return len(self.landmarks)

    # ------------------------------------------------------------------

    def __getitem__(self, index: int) -> Landmark:
        return self.landmarks[index]

    # ------------------------------------------------------------------

    def get(self, landmark_id: int) -> Landmark:
        """
        Return a landmark by its MediaPipe ID.
        """

        return self.landmarks[landmark_id]

    # ------------------------------------------------------------------

    @property
    def wrist(self) -> Landmark:
        return self.landmarks[0]

    @property
    def thumb_tip(self) -> Landmark:
        return self.landmarks[4]

    @property
    def index_tip(self) -> Landmark:
        return self.landmarks[8]

    @property
    def middle_tip(self) -> Landmark:
        return self.landmarks[12]

    @property
    def ring_tip(self) -> Landmark:
        return self.landmarks[16]

    @property
    def pinky_tip(self) -> Landmark:
        return self.landmarks[20]

    # ------------------------------------------------------------------

    @property
    def bounding_box(self) -> Tuple[float, float, float, float]:
        """
        Returns:

        (xmin, ymin, xmax, ymax)
        """

        xs = [lm.x for lm in self.landmarks]
        ys = [lm.y for lm in self.landmarks]

        return (
            min(xs),
            min(ys),
            max(xs),
            max(ys),
        )

    # ------------------------------------------------------------------

    @property
    def center(self) -> Tuple[float, float]:
        """
        Center of the hand.
        """

        xmin, ymin, xmax, ymax = self.bounding_box

        return (
            (xmin + xmax) / 2,
            (ymin + ymax) / 2,
        )

    # ------------------------------------------------------------------

    @property
    def width(self) -> float:

        xmin, _, xmax, _ = self.bounding_box

        return xmax - xmin

    # ------------------------------------------------------------------

    @property
    def height(self) -> float:

        _, ymin, _, ymax = self.bounding_box

        return ymax - ymin

    # ------------------------------------------------------------------

    @property
    def area(self) -> float:

        return self.width * self.height

    # ------------------------------------------------------------------

    def landmark_pixels(
        self,
        frame_width: int,
        frame_height: int,
    ) -> Dict[int, Tuple[int, int]]:
        """
        Returns all landmarks in pixel coordinates.
        """

        return {
            landmark.id: landmark.to_pixel(
                frame_width,
                frame_height,
            )
            for landmark in self.landmarks
        }

    # ------------------------------------------------------------------

    def distance(
        self,
        landmark_a: int,
        landmark_b: int,
    ) -> float:
        """
        Distance between two landmarks.
        """

        return self.landmarks[
            landmark_a
        ].distance_to(
            self.landmarks[
                landmark_b
            ]
        )

    # ------------------------------------------------------------------

    def contains(self, landmark_id: int) -> bool:

        return 0 <= landmark_id < len(self.landmarks)

    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        """
        Serialize the hand.
        """

        return {
            "label": self.label,
            "confidence": self.confidence,
            "landmarks": [
                {
                    "id": lm.id,
                    "x": lm.x,
                    "y": lm.y,
                    "z": lm.z,
                }
                for lm in self.landmarks
            ],
        }

    # ------------------------------------------------------------------

    @classmethod
    def empty(cls) -> "Hand":

        return cls(
            label="Unknown",
            confidence=0.0,
            landmarks=[],
        )

    # ------------------------------------------------------------------

    @property
    def is_left(self) -> bool:

        return self.label.lower() == "left"

    # ------------------------------------------------------------------

    @property
    def is_right(self) -> bool:

        return self.label.lower() == "right"

    # ------------------------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"Hand("
            f"label={self.label}, "
            f"confidence={self.confidence:.2f}, "
            f"landmarks={len(self.landmarks)})"
        )