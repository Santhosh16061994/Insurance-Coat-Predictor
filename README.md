# Insurance Cost Prediction

This project aims to develop a machine learning model for predicting insurance costs based on various factors such as age, gender, BMI, smoking habits, and region. By leveraging historical insurance data and machine learning algorithms, we strive to provide accurate cost estimates to insurance companies and individuals alike.

## Table of Contents

- [Project Overview](#project-overview)
- [Data Collection](#data-collection)
- [Feature Engineering](#feature-engineering)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Web Application](#web-application)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Insurance costs can vary significantly based on several factors, making accurate predictions crucial for insurance providers and policyholders. In this project, we aim to develop a machine learning model that analyzes key attributes such as age, gender, BMI, smoking habits, and region to predict insurance costs. By leveraging historical insurance data and employing various machine learning algorithms, we aim to provide accurate and personalized cost estimates.

## Data Collection

We collected a comprehensive dataset containing anonymized insurance records from diverse sources. The dataset includes attributes such as age, gender, BMI, number of children, smoking habits, and region. Rigorous data cleaning and preprocessing techniques were applied to handle missing values, outliers, and categorical variables.

## Feature Engineering

Feature engineering plays a vital role in developing an accurate insurance cost prediction model. We performed in-depth analysis of the dataset, identifying relevant features and transforming them to extract meaningful insights. Feature scaling, one-hot encoding, and other techniques were applied to prepare the data for training the models effectively.

## Model Training and Evaluation

We experimented with various machine learning algorithms, including linear regression, decision trees, random forests, and gradient boosting, to determine the most accurate model for insurance cost prediction. The dataset was split into training and testing sets, and we utilized cross-validation techniques to evaluate and fine-tune the models. Evaluation metrics such as mean squared error, mean absolute error, and R-squared were used to assess the models' performance.

## Web Application

To make our insurance cost prediction model accessible and user-friendly, we developed a web application using Streamlit, a Python library for creating interactive web interfaces. The web application allows users to input their relevant information, such as age, gender, BMI, smoking habits, and region, and obtain an estimated insurance cost. The application provides clear and interpretable results, empowering users to make informed decisions regarding their insurance needs.

Web app link : https://icpicp.streamlit.app/

## Dependencies

- Python 3.7 or higher
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## Installation

1. Clone the repository: `git clone https://github.com/your-username/insurance-cost-prediction.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Navigate to the project directory: `cd insurance-cost-prediction`
2. Launch the Streamlit web application: `streamlit run app.py`
3. Access the application in your web browser: `http://localhost:8501`

## Contributing

We welcome contributions to enhance the project and expand its functionality. If you encounter any issues or have suggestions for improvements, please submit a pull request or open an issue in the GitHub repository.


