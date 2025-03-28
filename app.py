import streamlit as st
import joblib

clf = joblib.load('loan_data.joblib')


st.title('LOAN APP BY DINESWAR')
g=st.number_input('Enter Gender 0:Male 1:Female')
m=st.number_input('Enter Martial status 0:No 1:Yes')
ai=st.number_input('Enter Loan amout in thousands')
la=st.number_input('Enter Loan amount thousands')

if st.button('PREDICT'):
    Prediction = clf.predict([[g,m,ai,la]])
    if Prediction == 'Y':
        st.text('LOAN IS APPROVED')
    else:
        st.text('LOAN IS REJUCTED')
