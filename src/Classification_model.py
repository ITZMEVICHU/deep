import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

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
    w1,col1,col2,w2= st.columns((.7,3,4,1))
    cc2,cc1,cc3=st.columns((1.5,7,.1))
    w111,col111,col222,w222= st.columns((.7,3,4,1))
    hy1,hy2,hy3,hy4,hy5=st.columns((.7,3,2,2,1))
    tr1,tr2,tr3,tr4= st.columns((.7,3,4,1))
    w1111,col1111,col2222,w2222= st.columns((.7,3,4,1))
    cc22,cc11,cc33=st.columns((1.5,7,.1))
    ee1,ee2,ee3,ee4= st.columns((.7,3,4,1))
    w4,col4,col44,w44= st.columns((.7,3,4,1))
    w5,col5,col55,w55= st.columns((.7,3,4,1))
    cc222,cc111,cc333=st.columns((1.5,7,.1))
    ex1,ex2,ex3= st.columns((1.5,7,.1))
    with col1:
        st.write("### ")
        st.write("## ")
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Training data upload</span></p>", unsafe_allow_html=True)
    
    with col2:
        
        vAR_input_training_data = st.file_uploader(' ',key='train')
        if vAR_input_training_data is not None:
            try:
                training_data = pd.read_excel(vAR_input_training_data)
                fs=training_data.drop(['Churn'], axis=1)
                colunms=fs.columns.values
            except BaseException as er:
                st.warning("Upload the correct training dataset")

            with w2:
                st.write("### ")
                st.write("## ")
                if st.button("Preview",key="prev11"):
                    with cc1:
                        st.write("# ")
                        st.write(training_data)
            
            # Data Preprocessing for Training Data
            training_data['Purchase Date'] = pd.to_datetime(training_data['Purchase Date'], format='%m%d%Y')
            label_encoder = LabelEncoder()
            training_data['Product'] = label_encoder.fit_transform(training_data['Product'])
            training_data['Gender'] = label_encoder.fit_transform(training_data['Gender'])

            scaler = StandardScaler()
            numerical_cols = ['Quantity', 'Price', 'Service Call', 'Service Failure Rate%', 'Customer Lifetime(Days)']
            training_data[numerical_cols] = scaler.fit_transform(training_data[numerical_cols])

            # Separating features and target variable for Training Data
            X_train = training_data.drop(['CustomerID', 'Purchase Date', 'Service Start Date', 'Churn'], axis=1)
            y_train = training_data['Churn']

            # Model Selection
            if vAR_input_model_type == 'Decision Trees':
                rf_classifier = DecisionTreeClassifier(random_state=42)
            elif vAR_input_model_type == 'Random Forest':
                rf_classifier = RandomForestClassifier(random_state=42)
            rf_classifier.fit(X_train, y_train)

            # Feature selection
            with col111:
                st.write("# ")
                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Feature Selection</span></p>", unsafe_allow_html=True)
            with col222:
                vAR_input_feature_selection = st.multiselect(' ',colunms,key='fetureselection')
            if vAR_input_feature_selection != []:
                with w222:
                    st.write("# ")
                    # st.write("# ")
                    # st.write("# ")
                    if st.button("Extract"):
                        with col222:
                            st.success("Extracted successfully")
            # Hyper parameter
            if vAR_input_feature_selection != []:
                with hy2:
                    st.write("# ")
                    st.write("# ")
                    st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Hyper Parameter</span></p>", unsafe_allow_html=True)
                with hy3:
                    st.write("# ")
                    random=st.number_input("Random state",value=42,step=3,min_value=10,max_value=90)
                with hy4:
                    st.write("# ")
                    hyper = st.selectbox('Method',["Select","Entropy","Gini"],key='hyper')
                if hyper != "Select":
                    with tr3:
                        st.write("# ")
                        if st.button("Train the Model"):
                            st.success("Training Process Completed")
                    
                    # Model Testing
                    with col1111:
                        st.write("### ")
                        st.write("## ")
                        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Test data upload</span></p>", unsafe_allow_html=True)
                    with col2222:
                        vAR_input_test_data = st.file_uploader(' ',key='test')
                    if vAR_input_test_data is not None:
                        try:
                            testing_data = pd.read_excel(vAR_input_test_data)
                            with w2222:
                                st.write("### ")
                                st.write("## ")
                                if st.button("Preview",key="prev1"):
                                    with cc11:
                                        st.write("# ")
                                        st.write(testing_data)
                            
                            
                            show_testing_data = pd.read_excel(vAR_input_test_data)
                            
                            # Data Preprocessing for Testing Data
                            testing_data['Product'] = label_encoder.fit_transform(testing_data['Product'])
                            testing_data['Gender'] = label_encoder.fit_transform(testing_data['Gender'])
                            testing_data[numerical_cols] = scaler.transform(testing_data[numerical_cols])

                            # Removing unwanted columns from Testing Data
                            X_test = testing_data.drop(['CustomerID', 'Purchase Date', 'Service Start Date', 'Reason for The customer to Churn / Non Churn'], axis=1)

                            # Predicting the target variable for Testing Data
                            y_pred_test = rf_classifier.predict(X_test)
                        except:
                            with ee3:
                                st.warning("Upload correct testing dataset")
                        else:
                            with col44:
                                st.write("")
                                if st.button("Test the Model"):
                                    st.success("Testing Process Completed")
                            with col5:
                                st.write("# ")
                                st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Result</span></p>", unsafe_allow_html=True)
                            
                            # Model Prediction
                            with col55:
                                result=st.selectbox("",["Select","Model Outcome","Explainable AI"])
                                if result != "Select":
                                    st.write("")
                                    if st.button("Submit"):
                                        if result == "Model Outcome":
                                            with cc111:
                                                selected_feature = show_testing_data[vAR_input_feature_selection]
                                                selected_feature['Predicted'] = y_pred_test
                                                st.write("# ")
                                                st.write(selected_feature)
                                        # Explainable AI
                                        with col55:
                                            if result =="Explainable AI":
                                                with ex2:
                                                    explain_model(rf_classifier, X_test)  # Assuming rf_classifier is your trained model
                            
