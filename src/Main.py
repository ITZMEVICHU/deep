import streamlit as st
import pandas as pd
from src.Classification_model import Classification_models
def prev1():
    st.session_state['preview1']="No"
def prev2():
    st.session_state['preview2']="No"
def prev3():
    st.session_state['preview3']="No"

def customerchurn():
    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement</span></p>", unsafe_allow_html=True)
    
    # Select box for problem statement
    vAR_input_problem_type = st.selectbox('', ['Customer Churn: Who is going to churn?'])

    if vAR_input_problem_type == 'Customer Churn: Who is going to churn?':
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Problem type</span></p>", unsafe_allow_html=True)
        
        # Select box for problem type
        vAR_input_type = st.selectbox('', ['Classification'])

        if vAR_input_type == 'Classification':
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Selection</span></p>", unsafe_allow_html=True)
            
            # Select box for Model selection
            vAR_input_model_type = st.selectbox('', ['Decision Trees', 'Random Forest'])

            if vAR_input_model_type != "Select":
                # Calling classification function and passing the selected model
                Classification_models(vAR_input_model_type)

if __name__ == "__main__":
    # Initialize Streamlit app
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

    st.markdown("<p style='text-align: center; color: black; font-size:23px;'><span style='font-weight: bold'>Learn to Build Industry Standard Data Science Applications</span></p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: blue;margin-top: -10px ;font-size:20px;'><span style='font-weight: bold'>MLOPS Built On Google Cloud and Streamlit</span></p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement:</span>Develop a Retail Machine Learning Applications (MLOPS): Customer Churn: Who is Going to Churn, When the Churn will Occur, Why it Occurs, and How to Prevent?</p>", unsafe_allow_html=True)
    st.markdown("<hr style=height:2.5px;margin-top:0px;background-color:gray;>",unsafe_allow_html=True)
    
    # Sidebar content here, if needed
    
    # Function to run the main app
    customerchurn()
