# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 00:56:47 2023

@author: Santhosh T N
"""


import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('model_pickle_test.pkl', 'rb'))


# Create the Streamlit app
st.title("Insurance Cost Prediction")
st.write("Enter the following information to predict insurance cost:")

# Create input fields for user input
age = st.slider("Age", 18, 100)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, step=0.1)
children = st.slider("Children", 0, 10)
smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

# Convert categorical input to numerical
sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0
region_mapping = {"Northeast": 0, "Northwest": 1, "Southeast": 2, "Southwest": 3}
region = region_mapping[region]

# Create a feature vector for prediction
input_data = [[age, sex, bmi, children, smoker, region]]

# Make prediction using the loaded model
prediction = loaded_model.predict(input_data)

# Display the predicted insurance cost
st.write("Predicted Insurance Cost:")
st.write(prediction)

