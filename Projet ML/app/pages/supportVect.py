import streamlit as st
import logging
import pickle

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
svmFile = open("SVM.pkl","rb")
modelSVM = pickle.load(svmFile)

def write():
    st.title("Support Vector Machine")

    # Take values from user
    with st.form(key='columns_in_form'):
        col1, col2, col3 = st.beta_columns(3)
        with col1:
            x1 = st.number_input("x1",format="%.3f")
            x4 = st.number_input("x4",format="%.3f")
            x7 = st.number_input("x7",format="%.3f")
        with col2:
            x2 = st.number_input("x2",format="%.3f")
            x5 = st.number_input("x5",format="%.3f")
            x8 = st.number_input("x8",format="%.3f")
        with col3:
            x3 = st.number_input("x3",format="%.3f")
            x6 = st.number_input("x6",format="%.3f")
            
        submit_button = st.form_submit_button('Submit')

    if submit_button:
        new_X_test = [[x1, x2, x3, x4, x5, x6, x7, x8]]
        new_y_pred = modelSVM.predict(new_X_test)

        # Display results to user
        if new_y_pred[0]==1:
            st.info("Good Quality")
        else :
            st.warning("Bad Quality")
