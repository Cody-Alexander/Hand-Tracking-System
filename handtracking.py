import cv2
import mediapipe as mp
import pyautogui as pag
import numpy as np
import time

# Initialize Mediapipe Hand solution
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=False, 
                       max_num_hands=2,
                       min_detection_confidence=0.1,
                       min_tracking_confidence=0.1)
 
mp_drawing = mp.solutions.drawing_utils

# Open camera
cap = cv2.VideoCapture(0)

# Error check to make sure camera is open
if not cap.isOpened():
    print("Error: Camera isn't open")
    exit()

# Set the screen resolution (width, height)
screen_width, screen_height = pag.size()

mouseDown = False
last_click_time = 0
click_delay = 0.5  # 500 milliseconds delay

# Main loop
while True:
    # Capture frame by frame from the camera 
    success, frame = cap.read() 
    if not success:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert the frame color from BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the RGB frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Frame resolution
    frame_height, frame_width, _ = frame.shape

    # Draw hand annotations on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Get the midpoint between the thumb and index finger
            midpoint_x = (index_finger_tip.x + thumb_tip.x) / 2
            midpoint_y = (index_finger_tip.y + thumb_tip.y) / 2

            # Get the distance between the thumb and index finger
            distance = np.sqrt((index_finger_tip.x - thumb_tip.x)**2 + (index_finger_tip.y - thumb_tip.y)**2)

            # Thresholds may need to be tuned
            current_time = time.time()
            if distance < 0.04 and not mouseDown and (current_time - last_click_time) > click_delay:
                # MouseDown
                pag.mouseDown()
                mouseDown = True
                last_click_time = current_time

            if distance > 0.05 and mouseDown:
                # MouseUp
                pag.mouseUp()
                mouseDown = False

            if mouseDown:
                cv2.circle(frame, (int(midpoint_x * frame_width), int(midpoint_y * frame_height)), 10, (0, 255, 0), -1)
            else:
                cv2.circle(frame, (int(midpoint_x * frame_width), int(midpoint_y * frame_height)), 10, (0, 255, 0), 1)

            # Map the position to the screen resolution
            x_mapped = np.interp(midpoint_x, (0, 1), (0, screen_width))
            y_mapped = np.interp(midpoint_y, (0, 1), (0, screen_height))
        
            # Set the mouse position
            pag.moveTo(x_mapped, y_mapped, duration=0.1)

    # Display the resulting frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
