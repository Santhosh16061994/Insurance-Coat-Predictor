# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 00:56:47 2023

@author: Santhosh T N
"""


import numpy as np
import pickle
import streamlit as st

# loading the saved model
model = pickle.load(open('C:/Users/Santhosh T N/OneDrive/Desktop/Deploy/Insurance/model_pickle_test.pkl', 'rb'))


html_temp = """
<div style="background-color:#f8f8f8;padding:10px;border-radius:10px">
<h3 style="color:#212529;text-align:center;">Insurance Cost Prediction</h3>
</div>
"""


def main():
    
    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    model = pickle.load(open('C:/Users/Santhosh T N/OneDrive/Desktop/Deploy/Insurance/model_pickle_test.pkl', 'rb'))
    
    


    
    # load the model
    
    p1 = st.slider("Enter Your Age",18,100)
    
    s1=st.selectbox("Sex",("Male","Female"))
    if s1=="Male":
        p2=1
    else:
        p2=0

    p3 =st.number_input("Enter Your BMI Value")
    p4 = st.slider("Enter Number of Children",0,4) 
    
    s2=st.selectbox("Smoker",("Yes","No"))
    if s2=="Yes":
        p5=1
    else:
        p5=0
        
    p6 = st.slider("Enter Your Region [1-4]",1,4)
    
    if st.button('Predict'):
        prediction = model.predict([[p1,p2,p3,p4,p5,p6]])
        st.balloons()
        st.success('Insurance Amount is {} '.format(round(prediction[0],2)))    
    
if __name__ == '__main__':
    main()