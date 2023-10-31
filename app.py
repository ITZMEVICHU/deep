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


st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement: Marketing managers at a retail company wanted to develop a targeted
marketing plan and demonstrate a return on investment (ROI) for their
marketing spend. To predict the customer's spending limit based on their
earnings and earning potential, the marketing team turned to their data
science team for a machine learning application (MLOps).</span></p>", unsafe_allow_html=True)
st.markdown("<hr style=height:2.5px;margin-top:0px;background-color:gray;>", unsafe_allow_html=True)

# Call the customerchurn function
if __name__ == "__main__":
    customerchurn()
