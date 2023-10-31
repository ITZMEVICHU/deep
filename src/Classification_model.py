import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures

def explain_model(model, X_test):
    # Create a SHAP explainer object
    explainer = shap.Explainer(model)
    
    # Compute SHAP values for a single prediction
    shap_values = explainer.shap_values(X_test)
    
    # Display the SHAP values with a plot
    shap.summary_plot(shap_values, X_test)
    st.pyplot(plt.gcf())

def Classification_models(vAR_input_model_type):
    # creating columns 
    w1, col1, col2, w2 = st.columns((.7, 3, 4, 1))
    cc2, cc1, cc3 = st.columns((1.5, 7, .1))
    w111, col111, col222, w222 = st.columns((.7, 3, 4, 1))
    hy1, hy2, hy3, hy4, hy5 = st.columns((.7, 3, 2, 2, 1))
    tr1, tr2, tr3, tr4 = st.columns((.7, 3, 4, 1))
    w1111, col1111, col2222, w2222 = st.columns((.7, 3, 4, 1))
    cc22, cc11, cc33 = st.columns((1.5, 7, .1))
    ee1, ee2, ee3, ee4 = st.columns((.7, 3, 4, 1))
    w4, col4, col44, w44 = st.columns((.7, 3, 4, 1))
    w5, col5, col55, w55 = st.columns((.7, 3, 4, 1))
    cc222, cc111, cc333 = st.columns((1.5, 7, .1))
    ex1, ex2, ex3 = st.columns((1.5, 7, .1))
    
    with col1:
        st.write("### ")
        st.write("## ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Training data upload</span></p>", unsafe_allow_html=True)

    with col2:
        vAR_input_training_data = st.file_uploader(' ', key='train')
        if vAR_input_training_data is not None:
            try:
                training_data = pd.read_csv(vAR_input_training_data)
                fs = training_data.drop(['spending_limit'], axis=1)
                columns = fs.columns.values
            except BaseException as er:
                st.warning("Upload the correct training dataset")

            with w2:
                st.write("### ")
                st.write("## ")
                if st.button("Preview", key="prev11"):
                    with cc1:
                        st.write("# ")
                        st.write(training_data)

            # Data Preprocessing for Training Data
            X = training_data[["earnings", "Savings"]]
            y = training_data["spending_limit"]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=34)

            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            poly = PolynomialFeatures(degree=2)
            X_train_poly = poly.fit_transform(X_train_scaled)
            X_test_poly = poly.transform(X_test_scaled)

            model = LinearRegression()
            model.fit(X_train_poly, y_train)

            y_pred_test = model.predict(X_test_poly)

            mse = mean_squared_error(y_test, y_pred_test)
            r2 = r2_score(y_test, y_pred_test)

            st.write("Mean Squared Error:", mse)
            st.write("R-squared:", r2)


            with col44:
                st.write("")
                if st.button("Test the Model"):
                    st.success("Testing Process Completed")
            with col5:
                st.write("# ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Result</span></p>", unsafe_allow_html=True)
                            
            # Model Prediction
           with col55:
        result = st.selectbox("", ["Select", "Model Outcome", "Explainable AI"])
        if result != "Select":
            st.write("")
            if st.button("Submit"):
                if result == "Model Outcome":
                    with cc111:
                        selected_feature = show_testing_data[vAR_input_feature_selection]
                        selected_feature['Predicted'] = y_pred_test
                        st.write("## ")
                        st.write(selected_feature)
                # Explainable AI
                with ex2:
                    if result == "Explainable AI":
                        explain_model(model, X_test_poly) 
