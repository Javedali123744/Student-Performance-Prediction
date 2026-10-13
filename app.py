import streamlit as st
import pandas as pd
import joblib

st.title("Student Performance Prediction")
st.write("Enter student details to predict the grade.")

model = joblib.load("student_grade_model.joblib")
features = joblib.load("feature_names.joblib")
options = joblib.load("feature_options.joblib")

student_data = {}

for feature in features:
    choices = options[feature]
    student_data[feature] = st.selectbox(
        feature,
        choices
    )

if st.button("Predict Grade"):
    input_df = pd.DataFrame([student_data])
    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Student Grade: {prediction}")