import streamlit as st
import time

progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.001)  # Simulate long-running computation
    progress_bar.progress(i + 1)  # Update progress bar

st.write('done!')