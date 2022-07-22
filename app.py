import streamlit as st
import pandas as pd

st.write("""
# Odd or even Number
This app tells whether the input is odd or even
""")

st.header('User Input Parameters')

def user_input_features():
  number = st.number_input("Number",min_value=0,max_value=2000000,step=1)

  data={'Number':number}
  features = pd.DataFrame(data, index=[0])
  return features


df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

if (int(df['Number'])%2==0):
  ans="Even"
else:
  ans="Odd"

st.subheader('The Number is:')
st.write(ans)
