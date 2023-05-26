import cv2
import streamlit as st
import numpy as np

# Load the Haar cascade xml files for face and eye
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

st.title("Webcam Live Feed")
run = st.checkbox('Run')

FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    if not ret:
        st.write('No frame captured. Make sure your webcam is connected and try again.')
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Sort eyes by x-coordinate
        eyes = sorted(eyes, key=lambda x: x[0])
        labels = ['Left eye', 'Right eye']
        
        for i, (label, (ex,ey,ew,eh)) in enumerate(zip(labels, eyes)):
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.putText(frame, f'{label} Open', (10, 30 + 30*i), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        if len(eyes) < 2:
            cv2.putText(frame, f'{label} Closed', (10, 30 + 30*i), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')

camera.release()

