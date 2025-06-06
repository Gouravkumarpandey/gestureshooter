# Gesture-Controlled Game Controller Using Hand Detection and Python

This project enables you to control PC games or browser-based games (e.g., [krunker.io](https://krunker.io)) using hand gestures detected in real-time via your webcam. The project uses MediaPipe for hand landmark detection and simulates keyboard and mouse inputs to interact with the game.

A webcam feed window is displayed on your screen with visual feedback of the detected hand landmarks, while the game runs side-by-side, allowing you to play using natural hand gestures.

---

## Features Implemented So Far

- **Real-time Hand Tracking:**
  - Uses [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) to detect and track hand landmarks from webcam video.
  - Visualizes detected hand landmarks and connections on webcam feed in an OpenCV window.

- **Gesture Recognition:**
  - Detects and differentiates three main gestures based on finger positions:
    - **Swipe Left (👈):** Identified by detecting leftward hand movement or specific finger pose.
    - **Pointing (🫵):** Index finger extended while others folded.
    - **Rock On (🤟):** Pinky and index finger extended, others folded.
  - Gesture detection logic includes basic landmark position analysis for reliable classification.

- **Input Simulation to Control Game:**
  - Maps each gesture to specific game controls:
    - Swipe Left → Press `S` (move backward)
    - Pointing → Press `W` (move forward)
    - Rock On → Left mouse click (shoot)
  - Uses Python’s `pyautogui` to simulate keyboard presses and mouse clicks.

- **Cooldown Mechanism:**
  - Implements a cooldown timer (e.g., 1 second) between repeated inputs to prevent flooding and unintended multiple actions when gesture is held.
  - Tracks last action time and only sends a new input if cooldown expired.

- **User Experience:**
  - Webcam feed window displays hand tracking in real-time.
  - User can open game window (browser for krunker.io or desktop game) and control it seamlessly.
  - Pressing `q` key exits the webcam feed and stops the program gracefully.

---

## Requirements

- Python 3.7+
- A webcam (built-in or external)
- Python packages:
  - `opencv-python`
  - `mediapipe`
  - `pyautogui`

Install all dependencies with:

```bash
pip install opencv-python mediapipe pyautogui
