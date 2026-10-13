# Student Performance Prediction

## About the Project
This project uses Machine Learning to predict student grades based on student-related information. It includes a web application built with Streamlit.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## Machine Learning Model
A Random Forest Classifier is used to predict student grades.

## Model Performance
- Test accuracy: 37.93%
- The dataset contains 145 student records and eight grade categories.
- The current result is a baseline and needs further improvement.

## How to Run
1. Install the required libraries:
   `pip install -r requirements.txt`
2. Train the model:
   `python train_model.py`
3. Start the web application:
   `python -m streamlit run app.py`

## Features
- Train a student grade prediction model.
- Enter student information through a web interface.
- Predict a student's grade.

## Disclaimer
This project is for educational purposes. Predictions may be inaccurate and should not be used as the sole basis for important educational decisions.
