"""Main module for the streamlit app"""
import streamlit as st
import awesome_streamlit as ast
import pages.home
import pages.knn
import pages.randomForest
import pages.gradientBoosting
import pages.decisionTree
import pages.naiveBayes
import pages.supportVect
import pages.logisticRegression


st.set_page_config(page_title='PC Quality')

ast.core.services.other.set_logging_format()


PAGES = {
    "Random Forest": pages.randomForest,
    "Logistic Regression": pages.logisticRegression,
    "K Nearest Neighbours": pages.knn,
    "Gradient Boosting": pages.gradientBoosting,
    "Decision Tree": pages.decisionTree,
    "Naive Bayes": pages.naiveBayes,
    "Support Vector Machine": pages.supportVect,
}


def main():

    st.sidebar.markdown(f'<p style="color:#002e91;font-size:28px;"><strong>Machine Learning</strong></p>', unsafe_allow_html=True)

    st.markdown(f'<p style="color:#6a0dad;font-size:40px;text-align:center;"><strong>PC Quality Prediction Using Machine Learning Models</strong></p>', unsafe_allow_html=True)

    # Display on webpage 
    st.sidebar.title("Steps for use: ")
    st.sidebar.markdown("1. Choose an algorithm from the list below")
    st.sidebar.markdown("2. Enter 8 values")
    st.sidebar.markdown("3. Press enter")
    st.sidebar.markdown("4. Wait for Good/Bad to appear")
    st.sidebar.markdown("It's that simple!")
    

    st.sidebar.title("Algorithmes")
    selection = st.sidebar.radio("Select Algorithm", list(PAGES.keys()))
    page = PAGES[selection]
    with st.spinner(f"Loading {selection} ..."):
        #page1 = st.markdown(f'<p style="color:#002e91;font-size:40px;text-align:center;"><strong>{page}</strong></p>', unsafe_allow_html=True)

        ast.shared.components.write_page(page)


    #st.text(""" The goal is to classify whether the breast cancer is benign or malignant. To achieve this i have used machine learning classification methods to fit a function that can predict the discrete class of new input. """)

if __name__ == "__main__":
    main()
