"""
logger.py

Application logger.
"""

from __future__ import annotations

import logging


class Logger:

    @staticmethod
    def create():

        logging.basicConfig(

            level=logging.INFO,

            format="%(asctime)s | %(levelname)s | %(message)s",

        )

        return logging.getLogger("GestureCam")