# """
# GestureCam

# Main application entry point.
# """

# from __future__ import annotations

# import cv2
# from src.actions.action_manager import ActionManager
# from src.actions.actions import Action

# from src.camera.camera_manager import CameraManager
# from src.camera.frame_processor import FrameProcessor

# from src.capture.countdown import Countdown
# from src.capture.photo_manager import PhotoManager

# from src.ui.overlay import Overlay
# from src.ui.window import Window

# from src.vision.gesture_detector import GestureDetector
# from src.vision.hand_tracker import HandTracker

# from config.settings import COUNTDOWN_SECONDS




# class GestureCam:

#     def __init__(self):
#         self.camera = CameraManager()
#         self.processor = FrameProcessor()
#         self.hand_tracker = HandTracker()
#         self.gesture_detector = GestureDetector()
#         self.action_manager = ActionManager()
#         self.photo_manager = PhotoManager()
#         self.countdown = Countdown(COUNTDOWN_SECONDS)
#         self.window = Window()
#         self.running = True
#         self.status = "Ready"
#         self.last_photo = None

#     # -----------------------------------------------------

#     def initialize(self):
#         self.camera.open()

#     # -----------------------------------------------------

#     def shutdown(self):
#         self.camera.release()
#         self.window.destroy()

#     # -----------------------------------------------------

#     def run(self):
#         self.initialize()
        
#         try:
#             while self.running:
#                 frame = self.camera.read()
#                 frame = self.processor.process(frame)
#                 fps = self.processor.update_fps()
#                 hands = self.hand_tracker.detect(frame)
#                 gesture = self.gesture_detector.detect(hands)
#                 action = self.action_manager.update(gesture)
                
#                 frame = self.handle_actions(frame, action)
#                 frame = Overlay.draw_title(frame)
#                 frame = Overlay.draw_gesture(frame, gesture.name)
#                 frame = Overlay.draw_status(frame, self.status)
#                 frame = Overlay.draw_fps(frame, fps)

#                 if self.countdown.running:
#                     frame = Overlay.draw_countdown(frame, self.countdown.remaining)

#                 self.window.show(frame)
#                 key = self.window.key()

#                 if self.window.should_close(key):
#                     break

#         finally:
#             self.shutdown()
    
#     # -----------------------------------------------------

#     def handle_actions(self, frame, action):
#         if action == Action.START_COUNTDOWN:
#             if not self.countdown.running:
#                 self.countdown.start()
#                 self.status = "Countdown..."

#         if self.countdown.running and self.countdown.update():
#             self.last_photo = self.photo_manager.save(frame)
#             frame = Overlay.flash(frame)
#             frame = Overlay.draw_saved(frame)
#             self.status = "Photo Saved"

#         if action == Action.CANCEL:
#             self.countdown.cancel()
#             self.status = "Cancelled"
#         elif action == Action.READY:
#             self.status = "Ready"
#         elif action == Action.FOCUS:
#             self.status = "Focus"
#         elif action == Action.CAPTURE:
#             self.last_photo = self.photo_manager.save(frame)
#             frame = Overlay.draw_saved(frame)
#             self.status = "Captured"

#         return frame


# def main():
#     app = GestureCam()
#     app.run()


# if __name__ == "__main__":
#     main()

"""
GestureCam

Main application entry point.
"""

from __future__ import annotations

import cv2
from src.actions.action_manager import ActionManager
from src.actions.actions import Action

from src.camera.camera_manager import CameraManager
from src.camera.frame_processor import FrameProcessor

from src.capture.countdown import Countdown
from src.capture.photo_manager import PhotoManager

from src.ui.overlay import Overlay
from src.ui.window import Window

from src.vision.frame_extractor import FrameExtractor
from src.vision.gesture_detector import GestureDetector
from src.vision.hand_tracker import HandTracker

from config.settings import COUNTDOWN_SECONDS




class GestureCam:

    def __init__(self):
        self.camera = CameraManager()
        self.processor = FrameProcessor()
        self.hand_tracker = HandTracker()
        self.gesture_detector = GestureDetector()
        self.frame_extractor = FrameExtractor()
        self.action_manager = ActionManager()
        self.photo_manager = PhotoManager()
        self.countdown = Countdown(COUNTDOWN_SECONDS)
        self.window = Window()
        self.running = True
        self.status = "Ready"
        self.last_photo = None

    # -----------------------------------------------------

    def initialize(self):
        self.camera.open()

    # -----------------------------------------------------

    def shutdown(self):
        self.camera.release()
        self.window.destroy()

    # -----------------------------------------------------

    def run(self):
        self.initialize()
        
        try:
            while self.running:
                frame = self.camera.read()
                frame = self.processor.process(frame)
                fps = self.processor.update_fps()
                hands = self.hand_tracker.detect(frame)
                capture = self.frame_extractor.get_capture_frame(
                    hands,
                    frame,
                )
                frame = self.frame_extractor.draw(
                    frame,
                    capture,
                )
                gesture = self.gesture_detector.detect(hands)
                action = self.action_manager.update(gesture)
                
                frame = self.handle_actions(frame, action)
                frame = Overlay.draw_title(frame)
                frame = Overlay.draw_gesture(frame, gesture.name)
                frame = Overlay.draw_status(frame, self.status)
                frame = Overlay.draw_fps(frame, fps)

                if self.countdown.running:
                    frame = Overlay.draw_countdown(frame, self.countdown.remaining)

                self.window.show(frame)
                key = self.window.key()

                if self.window.should_close(key):
                    break

        finally:
            self.shutdown()
    
    # -----------------------------------------------------

    def handle_actions(self, frame, action):
        if action == Action.START_COUNTDOWN:
            if not self.countdown.running:
                self.countdown.start()
                self.status = "Countdown..."

        if self.countdown.running and self.countdown.update():
            capture = self.frame_extractor.last_frame
            if capture is not None and capture.valid:
                self.last_photo = self.photo_manager.save_crop(
                    frame,
                    capture.x1,
                    capture.y1,
                    capture.x2,
                    capture.y2
                )
            else :
                capture = self.frame_extractor.last_frame
                if capture is not None and capture.valid:
                    self.last_photo = self.photo_manager.save_crop(
                        frame,
                        capture.x1,
                        capture.y1,
                        capture.x2,
                        capture.y2
                    )
                else:
                   self.last_photo = self.photo_manager.save(frame) 
            frame = Overlay.flash(frame)
            frame = Overlay.draw_saved(frame)
            self.status = "Photo Saved"

        if action == Action.CANCEL:
            self.countdown.cancel()
            self.status = "Cancelled"
        elif action == Action.READY:
            self.status = "Ready"
        elif action == Action.FOCUS:
            self.status = "Focus"
        elif action == Action.CAPTURE:
            self.last_photo = self.photo_manager.save(frame)
            frame = Overlay.draw_saved(frame)
            self.status = "Captured"

        return frame


def main():
    app = GestureCam()
    app.run()


if __name__ == "__main__":
    main()