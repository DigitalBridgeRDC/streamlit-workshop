import streamlit as st

st.sidebar.title('Streamlit Example: Sidebar')
option = st.sidebar.selectbox('Select an option', ['Option 1', 'Option 2', 'Option 3'])
st.sidebar.write(f'You selected: {option}')

if option == 'Option 1':
    st.title("You're number one!" )
