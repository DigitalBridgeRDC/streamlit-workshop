import streamlit as st
from PIL import Image

st.title('Astronaute on a Moonwalk')
image = Image.open('images/moonwalk.jpg')
st.image(image, caption='Moonwalk', use_column_width=True)
