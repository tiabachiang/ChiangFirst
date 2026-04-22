import streamlit as st
import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])

st.line_chart(data)

st.subheader('Select Box')

options = st.selectbox("What is your favourite colour?",('Red','Blue','Brown'))

st.write('Your choice of colour is:  ', options)
