import streamlit as st

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.header('Column 1')
    st.write('Some text...')
with col2:
    st.header('Column 2')
    st.write('Some text...')
with col3:
    st.header('Column 3')
    st.write('Some text...')
with col4:
    st.header('Column 4')
    st.write('Some text...')
