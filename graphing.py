import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sidebar for user to select the type of plot
plot_type = st.sidebar.selectbox('Select a type of plot', ['Scatter plot', 'Bar plot', 'Histogram', 'Boxplot', 'Line plot'])

# Depending on the user choice, display the corresponding plot
if plot_type == 'Scatter plot':
    df = pd.DataFrame(
        {'a': np.random.randn(1000),
        'b': np.random.randn(1000)})
    fig, ax = plt.subplots()
    ax.scatter(df['a'], df['b'])
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_title('Scatter Plot')

elif plot_type == 'Bar plot':
    df = pd.DataFrame({
        'Fruits' : ['Apple', 'Orange', 'Banana', 'Pear'],
        'Count' : [34, 51, 27, 14]
    })
    fig, ax = plt.subplots()
    ax.bar(df['Fruits'], df['Count'])
    ax.set_xlabel('Fruits')
    ax.set_ylabel('Count')
    ax.set_title('Bar Plot')

elif plot_type == 'Histogram':
    df = pd.DataFrame(
        {'a': np.random.randn(1000)})
    fig, ax = plt.subplots()
    ax.hist(df['a'], bins=30)
    ax.set_xlabel('a')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram')

elif plot_type == 'Boxplot':
    df = pd.DataFrame(
        {'a': np.random.randn(1000),
         'b': np.random.randn(1000) + 1})
    fig, ax = plt.subplots()
    ax.boxplot([df['a'], df['b']])
    ax.set_xticklabels(['a', 'b'])
    ax.set_ylabel('Values')
    ax.set_title('Boxplot')

elif plot_type == 'Line plot':
    df = pd.DataFrame({
        'Year' : range(2000, 2011),
        'Sales' : [9, 12, 15, 18, 26, 29, 35, 36, 38, 43, 47]
    })
    fig, ax = plt.subplots()
    ax.plot(df['Year'], df['Sales'])
    ax.set_xlabel('Year')
    ax.set_ylabel('Sales')
    ax.set_title('Line Plot')

st.pyplot(fig)
