import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("salary_model.pkl", "rb"))

# UI
st.set_page_config(page_title="Salary Predictor", layout="centered")

st.title("💼 Salary Prediction App")
st.write("Enter years of experience to predict salary")

# Input
experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=40.0,
    step=0.1
)

# Predict button
if st.button("Predict Salary"):
    prediction = model.predict([[experience]])
    
    st.success(f"💰 Estimated Salary: ₹ {prediction[0]:,.2f}")