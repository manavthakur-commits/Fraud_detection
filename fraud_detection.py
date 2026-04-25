import os
import streamlit as st
import pandas as pd
import joblib

model_path = "fraud_detection_model.pkl"
if not os.path.exists(model_path):
    model_path = "fraud_detection_pipeline.pkl"

model = joblib.load(model_path)

st.title("Fraud Detection Prediction App")

st.markdown("Please enter transaction details and use the predict button") 

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT","TRANSFER", "CASH_OUT", "DEPOSIT"])

amount = st.number_input("Amount", min_value=0.0, value = 1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value = 10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value = 9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value = 0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value = 0.0)
   
if st.button("Predict"):    
    input_data = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest]
    })
    
    prediction = model.predict(input_data)[0]
    result_text = "Fraudulent" if prediction == 1 else "Legitimate"

    st.subheader(f"Prediction Result: {result_text}")
    if prediction == 1:
        st.error("The transaction is predicted to be fraudulent.")
    else:
        st.success("The transaction is predicted to be legitimate.")  
        
         