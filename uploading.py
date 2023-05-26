import streamlit as st
import pandas as pd

# Display the file uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# If a file is uploaded
if uploaded_file is not None:
    # Load the contents of the file into a Pandas DataFrame
    dataframe = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.write(dataframe)

# ''' Excel
# uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])
# if uploaded_file is not None:
#     df = pd.read_excel(uploaded_file)
#     st.write(df)
# '''

# ''' text
# uploaded_file = st.file_uploader("Choose a text file", type="txt")
# if uploaded_file is not None:
#     text = uploaded_file.read().decode()
#     st.write(text)
# '''

# ''' Images
# from PIL import Image

# uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image)
# '''

#Python
uploaded_file = st.file_uploader("Choose a python file", type="py")
if uploaded_file is not None:
    code = uploaded_file.read().decode()
    st.code(code, language='python')
#

# ''' Videos
# uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mkv", "avi"])
# if uploaded_file is not None:
#     st.video(uploaded_file)

# '''