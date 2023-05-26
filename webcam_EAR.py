import cv2
import mediapipe as mp
import streamlit as st
import numpy as np

def calculate_ear(eye):
    A = np.linalg.norm(np.array(eye[1])-np.array(eye[5]))
    B = np.linalg.norm(np.array(eye[2])-np.array(eye[4]))
    C = np.linalg.norm(np.array(eye[0])-np.array(eye[3]))
    ear = (A + B) / (2.0 * C)
    return ear

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

EYE_AR_THRESH = 0.3

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    frame.flags.writeable = False
    results = face_mesh.process(frame)

    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    height, width, _ = frame.shape
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            left_eye_landmarks = [(int(lm.x * width), int(lm.y * height)) for lm in face_landmarks.landmark[133:143]]
            right_eye_landmarks = [(int(lm.x * width), int(lm.y * height)) for lm in face_landmarks.landmark[362:372]]
            
            left_eye_ear = calculate_ear(left_eye_landmarks)
            right_eye_ear = calculate_ear(right_eye_landmarks)

            ear = (left_eye_ear + right_eye_ear) / 2.0

            if ear < EYE_AR_THRESH:
                cv2.putText(frame, "Eyes closed", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                cv2.putText(frame, "Eyes open", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

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
