import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # If frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Our operations on the frame come here
    
    # Grayscale conversion
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gaussian blur
    blur = cv2.GaussianBlur(gray,(5,5),0)

    # Edge detection
    edges = cv2.Canny(blur, 50, 150)

    # Resize the image to half of original size
    resize = cv2.resize(edges, (0, 0), fx = 0.5, fy = 0.5) 

    # Display the resulting frame
    cv2.imshow('Webcam Feed', resize)

    # Quit if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
