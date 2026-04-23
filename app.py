import streamlit as st
import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])

st.line_chart(data)

st.subheader('Select Box')

options = st.selectbox("What is your favourite colour?",('Red','Blue','Brown'))

st.write('Your choice of colour is:  ', options)

st.subheader('*checkbox*')

icecream = st.checkbox('Icecream')
pizza = st.checkbox('pizza')
coffee = st.checkbox('coffee')

if icecream:
    st.write("Here is some more :icecream:")

if pizza:
    st.write("Here is some :pizza:")

if coffee:
    st.write("Here is some :coffee:")
