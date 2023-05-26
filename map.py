import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [[40.7128, -74.0060], [34.0522, -118.2437]],  # New York and Los Angeles
    columns=['lat', 'lon'])
st.write(df)
st.map(df)

data = {
    'City': ['Kinshasa', 'Lubumbashi', 'Mbuji-Mayi', 'Kananga', 'Kisangani', 'Bukavu', 'Goma', 'Kolwezi', 'Likasi', 'Boma'],
    'latitude': [-4.32758, -11.6646, -6.1360, -5.8966, 0.5167, -2.4914, -1.6596, -10.7167, -10.9704, -5.8467],
    'longitude': [15.3136, 27.4796, 23.5896, 22.4166, 25.2000, 28.8604, 29.2218, 25.4721, 26.7117, 13.0500]
}

df2 = pd.DataFrame(data)
st.write(df2)
st.map(df2)
