import cv2
import mediapipe as mp
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')

FRAME_WINDOW = st.image([])

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# For webcam input:
hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)

camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    # Flip the image horizontally
    frame = cv2.flip(frame, 1)
    # Convert the BGR image to RGB before processing
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # To improve performance, mark the image as not writeable to pass by reference
    frame.flags.writeable = False
    results = hands.process(frame)

    # Draw the hand annotations on the image
    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert back to BGR for rendering
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for Streamlit
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')

hands.close()
camera.release()
