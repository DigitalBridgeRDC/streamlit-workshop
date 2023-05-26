import streamlit as st
import pandas as pd

st.title('Diplaying dataframes')

st.header('first dataframe')
# Create a simple dataframe
df = pd.DataFrame({
  'A': [1, 2, 3, 4, 5],
  'B': ['a', 'b', 'c', 'd', 'e'],
})

st.write(df)

st.header('Dem. Rep. Congo Cities')
# DRC main cities lat and long coordinates
data = {
    'city': ['Kinshasa', 'Lubumbashi', 'Mbuji-Mayi', 'Kananga', 'Kisangani', 'Bukavu', 'Goma', 'Kolwezi', 'Likasi', 'Boma'],
    'latitude': [-4.32758, -11.6646, -6.1360, -5.8966, 0.5167, -2.4914, -1.6596, -10.7167, -10.9704, -5.8467],
    'longitude': [15.3136, 27.4796, 23.5896, 22.4166, 25.2000, 28.8604, 29.2218, 25.4721, 26.7117, 13.0500]
}

df2 = pd.DataFrame(data)

st.write(df2)
