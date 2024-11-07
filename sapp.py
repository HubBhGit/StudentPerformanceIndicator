import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Title of the Streamlit application
st.title("Student Exam Performance Indicator")

# User input form
st.header("Student Exam Performance Prediction")

# Gender selection
gender = st.selectbox("Gender", options=["Select your Gender", "male", "female"], index=0)

# Race or Ethnicity selection
ethnicity = st.selectbox("Race or Ethnicity", options=["Select Ethnicity", "group A", "group B", "group C", "group D", "group E"], index=0)

# Parental Level of Education selection
parental_level_of_education = st.selectbox(
    "Parental Level of Education", 
    options=[
        "Select Parent Education", 
        "associate's degree", 
        "bachelor's degree", 
        "high school", 
        "master's degree", 
        "some college", 
        "some high school"
    ],
    index=0
)

# Lunch type selection
lunch = st.selectbox("Lunch Type", options=["Select Lunch Type", "free/reduced", "standard"], index=0)

# Test preparation course selection
test_preparation_course = st.selectbox("Test Preparation Course", options=["Select Test Course", "none", "completed"], index=0)

# Reading Score input
reading_score = st.number_input("Reading Score (out of 100)", min_value=0, max_value=100, step=1)

# Writing Score input
writing_score = st.number_input("Writing Score (out of 100)", min_value=0, max_value=100, step=1)

# Prediction button
if st.button("Predict your Math Score"):
    # Check if all inputs are selected
    if gender == "Select your Gender" or ethnicity == "Select Ethnicity" or parental_level_of_education == "Select Parent Education" or lunch == "Select Lunch Type" or test_preparation_course == "Select Test Course":
        st.error("Please make sure all fields are selected.")
    else:
        # Collect data in CustomData format
        data = CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        # Convert data to DataFrame
        pred_df = data.get_data_as_data_frame()
        st.write("Input Data:", pred_df)  # Display the DataFrame for confirmation

        try:
            # Initialize the prediction pipeline and make predictions
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)

            # Display the result
            st.success(f"The predicted math score is {results[0]}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
