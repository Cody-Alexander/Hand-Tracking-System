# Hand-Tracking-System
This project uses hand gestures to control the mouse cursor on your screen. It utilizes the MediaPipe library for hand tracking and PyAutoGUI for mouse control. The code captures video from your camera, processes hand landmarks, and maps hand movements to the mouse cursor. I have adjusted this in order to better suit my system

## Features

- **Hand Tracking**: Detects and tracks hand landmarks in real-time using MediaPipe.
- **Mouse Control**: Moves the mouse cursor based on the position of the hand and simulates mouse clicks with gestures.
- **Gesture Detection**: Uses the distance between the thumb and index finger to detect mouse clicks.

## Requirements

- Python 3.12
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- PyAutoGUI (`pyautogui`)
- NumPy (`numpy`)

You can install the required libraries using pip:

```bash
pip install opencv-python mediapipe pyautogui numpy
```

## Usage

1. **Run the Script**: Execute the script to start capturing video from your camera and control the mouse using hand gestures.

    ```bash
    python hand_gesture_mouse_control.py
    ```

2. **Control the Mouse**:
   - **Move Cursor**: Position your hand in front of the camera, and move it to control the cursor.
   - **Click**: Bring your thumb and index finger close together to simulate a mouse click.

3. **Stop the Program**: Press 'q' to quit the application.

## Code Overview

- **MediaPipe Initialization**: Sets up MediaPipe's Hand solution to detect and track hand landmarks.
- **Video Capture**: Opens the camera and processes each frame to detect hand gestures.
- **Gesture Detection**: Calculates the distance between the thumb and index finger to simulate mouse clicks.
- **Mouse Movement**: Maps hand movements to screen coordinates and moves the mouse cursor accordingly.

## Troubleshooting

- **Camera Not Opening**: Ensure your camera is connected and not being used by another application.
- **Hand Detection Issues**: Make sure you have good lighting and the camera is positioned to clearly capture your hands.
