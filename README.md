# GestureCam

GestureCam is a real-time gesture-controlled camera application developed using Python, OpenCV, and MediaPipe. It enables users to interact with a webcam without touching the keyboard or mouse by recognizing hand gestures and translating them into camera actions.

The application detects predefined hand gestures in real time, displays visual feedback through an interactive interface, and allows users to capture only a selected region defined by their hands. To improve the visual quality of captured images, GestureCam also includes a lightweight real-time beauty filter.

---

## Features

- Real-time hand detection using MediaPipe Hands
- Gesture recognition for camera control
- Touch-free image capture
- Countdown timer before capturing images
- Virtual capture frame created using two hands
- Region-of-interest (ROI) extraction based on the virtual frame
- Automatic cropping of the selected area
- Real-time beauty filter with skin smoothing and color enhancement
- Live interface displaying:
  - Current gesture
  - Application status
  - FPS
  - Countdown timer
  - Virtual capture frame
- Automatic image saving with timestamped filenames

---

## Supported Gestures

| Gesture | Action |
|----------|--------|
| Open Hand | Ready |
| Fist | Cancel |
| Thumbs Up | Capture Immediately |
| Peace | Save |
| Pinch | Focus |
| Two-Hand Frame | Start Countdown and Capture Selected Region |

---

## System Architecture

```
GestureCam/
│
├── src/
│   ├── actions/
│   ├── camera/
│   ├── capture/
│   ├── config/
│   ├── ui/
│   ├── vision/
│   └── main.py
│
├── captures/
├── config/
├── requirements.txt
└── README.md
```

---

## Technologies

- Python 3.12
- OpenCV
- MediaPipe
- NumPy

---

## Installation

Clone the repository.

```bash
git clone https://github.com/asmaBelkerrouche/GestureCam.git
```

Move into the project directory.

```bash
cd GestureCam
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the project from the root directory.

```bash
python -m src.main
```

---

## Workflow

1. Capture frames from the webcam.
2. Detect hands using MediaPipe.
3. Extract hand landmarks.
4. Recognize predefined gestures.
5. Generate a virtual capture frame using both hands.
6. Display a countdown before capture.
7. Crop only the selected region.
8. Apply the beauty filter.
9. Save the final image automatically.

---

## Beauty Filter

GestureCam includes a lightweight image enhancement pipeline implemented with OpenCV.

The filter performs:

- Skin smoothing using bilateral filtering
- Brightness enhancement
- Contrast adjustment
- Slight color enhancement

The processing is performed in real time while maintaining interactive frame rates.

---

## Output

Captured images are automatically stored in the `photos/` directory.

Example filename:

```
photo_2026-07-10_14-32-18.jpg
```

---

## Future Enhancements

Potential improvements include:

- Face beautification using MediaPipe Face Mesh
- Background segmentation and portrait mode
- Custom gesture configuration
- Video recording
- AI-based gesture classification
- Face authentication
- Cloud image synchronization
- Multi-camera support

---

## Educational Objectives

This project demonstrates concepts in:

- Computer Vision
- Human-Computer Interaction
- Real-Time Image Processing
- Gesture Recognition
- MediaPipe Hand Tracking
- OpenCV
- Object-Oriented Software Design

---

## Author

**Asma Belkerrouche**

Computer Engineering Student — Cybersecurity Specialization

École Supérieure en Sciences et Technologies de l'Informatique et du Numérique (ESTIN)

---

## License

This project was developed for educational and academic purposes.
