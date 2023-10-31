import streamlit as st
import os
from src.Main import customerchurn

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    body {
        zoom: 90%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

from PIL import Image
import os

with open('style/final.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

imcol1, imcol2, imcol3 = st.columns((4, 5, 3))
with imcol1:
    st.write("")
with imcol2:
    st.image('image/ds.png')

with imcol3:
    st.write("")


st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: Develop a Retail Machine Learning Applications (MLOPS): Customer Churn: Who is Going to Churn, When the Churn will Occur, Why it Occurs, and How to Prevent?</span></p>", unsafe_allow_html=True)
st.markdown("<hr style=height:2.5px;margin-top:0px;background-color:gray;>", unsafe_allow_html=True)

# Call the customerchurn function
if __name__ == "__main__":
    customerchurn()
