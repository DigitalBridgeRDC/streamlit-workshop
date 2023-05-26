import streamlit as st

# Title
st.title("Streamlit Sample App Tutorial")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is some text kwerjheijhjfgiwejhttfgijhi9rwe9jhg.")

# Markdown
st.markdown("### This is a markdown heading")
st.markdown("_This_ is some ***bold*** text.")

# Displaying data
data = {
    'Name': ['John', 'Jane', 'Bill'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
st.dataframe(data)

# Interactive widgets
option = st.selectbox("Choose an option", ["Red", "Orange", "Green"])
st.write("You selected:", option)

if option=='Green':
    st.write('Digital Bridge is awesome!')

slider_value = st.slider("Select a value", 20, 2000, 150)
st.write("Slider value:", slider_value)

# Buttons
if st.button("Hit me now!"):
    st.write("Button clicked!")
    

# Checkbox
if st.checkbox("Check me"):
    st.write("Checkbox checked!")
if st.checkbox("Check me too"):
    st.write("Checkbox checked!")
if st.checkbox("Check me too, please"):
    st.write("Checkbox checked!")

# Radio buttons
radio_value = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", radio_value)

# Text input
text_input = st.text_input("Enter some text")
st.write("Text entered:", text_input)

# File upload
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")

# Progress bar
import time

progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress_bar.progress(i + 1)

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.subheader("This is a sidebar.")
st.sidebar.text("You can add content here.")

# Plotting
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
st.pyplot(plt)

# Displaying images
from PIL import Image

image = Image.open('images/moonwalk.jpg')
st.image(image, caption="Sample Image", use_column_width=True)
