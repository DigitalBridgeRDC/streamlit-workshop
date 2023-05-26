import streamlit as st
from PIL import Image
import io

# Define function to display image
def display_image(image):
    st.image(image, use_column_width=True)

# Define function to display video
def display_video(video_bytes):
    st.video(video_bytes)

# Create sidebar with selection options
selection = st.sidebar.selectbox("Select an option", ("Image", "Video"))

if selection == "Image":
    st.header("Display Image")
    image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if image_file is not None:
        # Read the uploaded image file
        image = Image.open(image_file)
        display_image(image)

elif selection == "Video":
    st.header("Display Video")
    video_file = st.file_uploader("Upload a video", type=["mp4"])

    if video_file is not None:
        # Read the uploaded video file
        video_bytes = video_file.read()
        display_video(video_bytes)

