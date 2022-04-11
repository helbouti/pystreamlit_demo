"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
#st.camera_input("Take a picture")

st.button("button1")

st.selectbox("List des Producteurs",["abida khaled","abida sid ahmed","abida lakhdar"],index=1)

col1,col2=st.columns(2)

with col1:
    bt1=st.button("col1 button")
    if bt1:
        st.write("bt1 clicked")
        


with col2:
    bt2=st.button("col2 button")
    if bt2:
      st.balloons()
      st.success("congratulation....")
