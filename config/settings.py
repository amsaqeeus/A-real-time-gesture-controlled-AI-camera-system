"""
settings.py

Global configuration for GestureCam.
"""

from pathlib import Path

# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

PHOTO_FOLDER = BASE_DIR / "captures"

PHOTO_PREFIX = "gesturecam"

IMAGE_EXTENSION = ".jpg"

# ---------------------------------------------------------
# Camera
# ---------------------------------------------------------

CAMERA_INDEX = 0

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

FPS = 30

WINDOW_NAME = "GestureCam"

# ---------------------------------------------------------
# Capture
# ---------------------------------------------------------

COUNTDOWN_SECONDS = 3

# ---------------------------------------------------------
# UI
# ---------------------------------------------------------

FONT_SIZE = 0.8

LINE_THICKNESS = 2

# ---------------------------------------------------------
# MediaPipe
# ---------------------------------------------------------

MAX_NUM_HANDS = 2

MIN_DETECTION_CONFIDENCE = 0.7

MIN_TRACKING_CONFIDENCE = 0.7

# ---------------------------------------------------------
# Colors (BGR)
# ---------------------------------------------------------

COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "GREEN": (0, 255, 0),
    "RED": (0, 0, 255),
    "BLUE": (255, 0, 0),
    "YELLOW": (0, 255, 255),
    "CYAN": (255, 255, 0),
    "ORANGE": (0, 165, 255),
}