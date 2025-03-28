import streamlit as st
import joblib

clf = joblib.load('loan_data.joblib')


st.title('LOAN APP BY DINESWAR')
g=st.selectbox('Select an gender:',['Male','Female'])
m=st.selectbox('Select Marriage status: ',['No','Yes'])
ai=st.number_input('Enter annual income (in thousands)')
la=st.number_input('Enter Loan amount (in thousands)')
gfinal = 0 if g == 'Male' else 1
marriage= 0 if  m == 'No' else 1

if st.button('PREDICT'):
    Prediction = clf.predict([[gfinal,marriage,ai,la]])
    if Prediction == 'Y':
        st.text('LOAN IS APPROVED')
    else:
        st.text('LOAN IS REJECTED')
