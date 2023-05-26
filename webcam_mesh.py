import cv2
import mediapipe as mp
import streamlit as st

st.title("Webcam Live Feed")
run = st.checkbox('Run')

FRAME_WINDOW = st.image([])

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# For webcam input:
face_mesh = mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)

camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    # Flip the image horizontally for a better selfie-view display, and convert
    # the BGR image to RGB
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

    # To improve performance, mark the image as not writeable to pass by reference
    frame.flags.writeable = False
    results = face_mesh.process(frame)

    # Draw the face mesh annotations on the image
    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=frame, 
                landmark_list=face_landmarks, 
                connections=None,  # No connections defined for facemesh
                landmark_drawing_spec=drawing_spec, 
                connection_drawing_spec=None
            )

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for Streamlit
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')

face_mesh.close()
camera.release()
