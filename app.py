
import streamlit as st
import pandas as pd
import joblib

# Load the trained machine learning model
model = joblib.load("model.pkl")

# Website title
st.title("Student Performance Predictor")

# Description
st.write("Enter student details to predict final examination marks.")

# Input fields
study_hours = st.slider("Study Hours Per Day", 0, 12, 5)

attendance = st.slider("Attendance Percentage", 0, 100, 80)

previous_score = st.slider("Previous Exam Marks", 0, 100, 70)

sleep_hours = st.slider("Sleep Hours Per Day", 0, 12, 7)

# Prediction button
if st.button("Predict Performance"):

    # Prepare input data
    input_data = pd.DataFrame(
        [[study_hours, attendance, previous_score, sleep_hours]],
        columns=[
            "study_hours",
            "attendance",
            "previous_score",
            "sleep_hours"
        ]
    )

    # Predict final marks
    prediction = model.predict(input_data)[0]

    # Display result
    st.success("Prediction Completed!")

    st.metric("Predicted Final Marks", f"{prediction:.2f} / 100")

    # Performance category
    if prediction >= 80:
        st.write("Performance: Excellent")
    elif prediction >= 60:
        st.write("Performance: Good")
    elif prediction >= 40:
        st.write("Performance: Average")
    else:
        st.write("Performance: Needs Improvement")
