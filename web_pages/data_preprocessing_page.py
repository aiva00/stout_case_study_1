import streamlit as st
from web_pages.page_abstract import Page


class DataPreprocessing(Page):

    def __init__(self) -> None:
        super().__init__()

    def main(self) -> None:
        st.title('Data Preprocessing')

        st.markdown("""
                    In the "Data Cleaning" page we made it clear that decision-tree-based models achieve the highest performance on tabular data for regression.  
                      
                    These models have additional benefits that solidify them as the best candidate.
                    - They are scale invariant. Since they are probabilistic models, scaling the features will have no impact on the model
                    - Robust to outliers
                    - Can handle NA's way easier. In decision trees one can carefully impute missing values using extreme values or other unexpected ones.
                    """)
        st.markdown('In this project we are going to try a lot of different models and so, all these operations will be performed in order to assist the distance-based models')

        st.markdown('# Train Val Test Split')
        st.markdown("""
                    Train test split must be used in order to validate that our model generalizes well.  
                    We use the validation set as a way to find the best hyperparameters of the model and perform all of our test. The test is only used in the end and is left untouched.
                    In addition, we need to create the split before the scaling, imputing and encoding, to have realistic results and simulate real world evaluation
                    """)

        st.markdown('# Encoding Categorical Variables')
        st.markdown("""
                    Machine Learning algorithms need numeric data in order to function. This is why the encoding of categorical variables is essential for analysis.  
                    I opted to go with Binary Encoder instead of the classic methods such as One-Hot-Encoding and Ordinal Encoding.  
                    - One-Hot-Encoding creates too many features (1 for each category in the feature) and in our case that would create a lot of additional features and may lead to the curse of dimensionality
                    - Ordinal Encoding assumes that there is an order in the categories of a feature.  
                    Binary Encoding on the other hand creates way less categories while trying to retain as much information as possible.  
                    The encoded dataset contains 69 columns after encoding.
                    """)

        st.markdown('# Handle NA\'s')
        st.markdown("""
                    Some features mostly consist of missing values ( > 50%). Of course it would be unwise to include these in the modelling phase of the project, since imputing these values would be highly inaccurate and introduce a lot of bias and noise in our data. If this was a real project we would need to identify the reasons that these values were missing, find out if there is a problem, analyze the features further and try to encode the information somehow, but for now we can just drop. An easy fix for a discrete feature like ‘verification_income_joint’ is to create another category named “Missing” that contains all the missing datapoints of the column.  
                      
                    For the remaining features that contain a smaller percentage of missing values we can use a Simple Imputer to impute them, but further tests should be made to make sure that we don’t introduce bias to the dataset, and find a better imputation technique.  
                      
                    The truth though is that we will end up with a decision tree based algorithm, and those can handle missing values a lot better, giving the option to carefully encode them into a specific value (maybe out of range, or really extreme), preventing bias and information loss, but we will just use the imputer for now.

                    """)

        st.markdown('# Scaling')
        st.markdown("""
                    Standard Scaler was used in order to center the mean of the features around 0. More advanced scaling techniques could be tried but due to the limitation in time this was considered enough.
                    """)

        st.markdown('# Feature Selection')
        st.markdown("""
                    Algorithms like Recursive Feature Elimination could be tried to select the optimal features.  
                    I didn't implement them for 2 main reasons.
                    1. Lack of business domain knowledge. I didn't want to drop features that I don't really know their value, and an expert should be consulted
                    2. The dataset is already small enough so reducing complexity won't really have an impact for now
                    """)

    def load_page(self) -> None:

        self.main()
