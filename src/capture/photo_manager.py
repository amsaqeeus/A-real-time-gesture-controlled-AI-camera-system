# """
# photo_manager.py

# Handles saving captured images.
# """

# from __future__ import annotations

# from datetime import datetime
# from pathlib import Path

# import cv2
# import numpy as np

# from config.settings import (
#     PHOTO_FOLDER,
#     PHOTO_PREFIX,
#     IMAGE_EXTENSION,
# )


# class PhotoManager:
#     """
#     Manages photo saving operations.
#     """

#     def __init__(
#         self,
#         output_directory: Path = PHOTO_FOLDER,
#     ) -> None:

#         self.output_directory = output_directory

#         self.output_directory.mkdir(
#             parents=True,
#             exist_ok=True,
#         )

#     # ---------------------------------------------------------

#     def generate_filename(self) -> str:
#         """
#         Generate a unique filename.
#         """

#         timestamp = datetime.now().strftime(
#             "%Y-%m-%d_%H-%M-%S"
#         )

#         return (
#             f"{PHOTO_PREFIX}_"
#             f"{timestamp}"
#             f"{IMAGE_EXTENSION}"
#         )

#     # ---------------------------------------------------------

#     def save(
#         self,
#         frame: np.ndarray,
#     ) -> Path:
#         """
#         Save a frame to disk.
#         """

#         filepath = (
#             self.output_directory
#             / self.generate_filename()
#         )

#         success = cv2.imwrite(
#             str(filepath),
#             frame,
#         )

#         if not success:
#             raise IOError(
#                 "Failed to save image."
#             )

#         return filepath

#     # ---------------------------------------------------------

#     def exists(
#         self,
#         filename: str,
#     ) -> bool:

#         return (
#             self.output_directory / filename
#         ).exists()

#     # ---------------------------------------------------------

#     def delete(
#         self,
#         filename: str,
#     ) -> bool:

#         file = self.output_directory / filename

#         if not file.exists():
#             return False

#         file.unlink()

#         return True

#     # ---------------------------------------------------------

#     def list_images(self) -> list[Path]:

#         return sorted(
#             self.output_directory.glob(
#                 f"*{IMAGE_EXTENSION}"
#             )
#         )

#     # ---------------------------------------------------------

#     def count(self) -> int:

#         return len(
#             self.list_images()
#         )

"""
photo_manager.py

Handles saving captured images.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import cv2
import numpy as np

from config.settings import (
    PHOTO_FOLDER,
    PHOTO_PREFIX,
    IMAGE_EXTENSION,
)


class PhotoManager:
    """
    Manages photo saving operations.
    """

    def __init__(
        self,
        output_directory: Path = PHOTO_FOLDER,
    ) -> None:

        self.output_directory = output_directory

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    # ---------------------------------------------------------

    def generate_filename(self) -> str:

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        return (
            f"{PHOTO_PREFIX}_"
            f"{timestamp}"
            f"{IMAGE_EXTENSION}"
        )

    # ---------------------------------------------------------

    def save(
        self,
        frame: np.ndarray,
    ) -> Path:

        filepath = (
            self.output_directory
            / self.generate_filename()
        )

        success = cv2.imwrite(
            str(filepath),
            frame,
        )

        if not success:
            raise IOError(
                "Failed to save image."
            )

        return filepath

    # ---------------------------------------------------------

    def save_crop(
        self,
        frame: np.ndarray,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> Path:
        """
        Save only the selected rectangle.
        """

        h, w = frame.shape[:2]

        x1 = max(0, min(x1, w))
        x2 = max(0, min(x2, w))

        y1 = max(0, min(y1, h))
        y2 = max(0, min(y2, h))

        if x2 <= x1 or y2 <= y1:
            raise ValueError(
                "Invalid crop coordinates."
            )

        crop = frame[
            y1:y2,
            x1:x2,
        ]

        if crop.size == 0:
            raise ValueError(
                "Crop is empty."
            )

        filepath = (
            self.output_directory
            / self.generate_filename()
        )

        success = cv2.imwrite(
            str(filepath),
            crop,
        )

        if not success:
            raise IOError(
                "Failed to save cropped image."
            )

        return filepath

    # ---------------------------------------------------------

    def exists(
        self,
        filename: str,
    ) -> bool:

        return (
            self.output_directory / filename
        ).exists()

    # ---------------------------------------------------------

    def delete(
        self,
        filename: str,
    ) -> bool:

        file = self.output_directory / filename

        if not file.exists():
            return False

        file.unlink()

        return True

    # ---------------------------------------------------------

    def list_images(self) -> list[Path]:

        return sorted(
            self.output_directory.glob(
                f"*{IMAGE_EXTENSION}"
            )
        )

    # ---------------------------------------------------------

    def count(self) -> int:

        return len(
            self.list_images()
        )