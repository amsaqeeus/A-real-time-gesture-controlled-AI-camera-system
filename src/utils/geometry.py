"""
geometry.py

Geometric utility functions for GestureCam.
"""

from __future__ import annotations

from math import acos, degrees, sqrt

from src.vision.landmark import Landmark


class Geometry:
    """Geometry helper functions."""

    @staticmethod
    def distance(
        point1: Landmark,
        point2: Landmark,
    ) -> float:
        """
        Euclidean distance between two landmarks.
        """

        return sqrt(
            (point1.x - point2.x) ** 2
            + (point1.y - point2.y) ** 2
            + (point1.z - point2.z) ** 2
        )

    # ---------------------------------------------------------

    @staticmethod
    def midpoint(
        point1: Landmark,
        point2: Landmark,
    ) -> tuple[float, float]:

        return (
            (point1.x + point2.x) / 2,
            (point1.y + point2.y) / 2,
        )

    # ---------------------------------------------------------

    @staticmethod
    def hand_size(hand) -> float:
        """
        Approximate hand size using wrist → middle fingertip.
        """

        return Geometry.distance(
            hand.wrist,
            hand.middle_tip,
        )

    # ---------------------------------------------------------

    @staticmethod
    def normalized_distance(
        point1: Landmark,
        point2: Landmark,
        hand,
    ) -> float:

        size = Geometry.hand_size(hand)

        if size == 0:
            return 0.0

        return Geometry.distance(
            point1,
            point2,
        ) / size

    # ---------------------------------------------------------

    @staticmethod
    def angle(
        a: Landmark,
        b: Landmark,
        c: Landmark,
    ) -> float:
        """
        Returns angle ABC in degrees.
        """

        ab = (
            a.x - b.x,
            a.y - b.y,
            a.z - b.z,
        )

        cb = (
            c.x - b.x,
            c.y - b.y,
            c.z - b.z,
        )

        dot = (
            ab[0] * cb[0]
            + ab[1] * cb[1]
            + ab[2] * cb[2]
        )

        mag_ab = sqrt(
            ab[0] ** 2
            + ab[1] ** 2
            + ab[2] ** 2
        )

        mag_cb = sqrt(
            cb[0] ** 2
            + cb[1] ** 2
            + cb[2] ** 2
        )

        if mag_ab == 0 or mag_cb == 0:
            return 0.0

        cosine = dot / (mag_ab * mag_cb)

        cosine = max(-1.0, min(1.0, cosine))

        return degrees(
            acos(cosine)
        )

    # ---------------------------------------------------------

    @staticmethod
    def is_close(
        point1: Landmark,
        point2: Landmark,
        hand,
        threshold: float = 0.15,
    ) -> bool:

        return (
            Geometry.normalized_distance(
                point1,
                point2,
                hand,
            )
            < threshold
        )

    # ---------------------------------------------------------

    @staticmethod
    def center(hand):

        xmin, ymin, xmax, ymax = hand.bounding_box

        return (
            (xmin + xmax) / 2,
            (ymin + ymax) / 2,
        )

    # ---------------------------------------------------------

    @staticmethod
    def bounding_box(hand):

        return hand.bounding_box