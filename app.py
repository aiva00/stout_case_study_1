import streamlit as st
from web_pages.data_cleaning_page import DataCleaning
from web_pages.home_page import Home
from web_pages.data_preprocessing_page import DataPreprocessing
from web_pages.outlier_detection_page import OutlierDetection
from web_pages.modelling_page import Modeling
from web_pages.explainability_page import Explainability
from web_pages.visualization_page import Visualization

# Streamlit Config

with st.sidebar:
    page = st.radio(
        label='Navigation',
        options=['Home', 'Data Cleaning', 'Data Preprocessing',
                 'Outlier Detection', 'Modelling', 'Explainable AI', 'Visualization'],
        key='nav_radio',
        help='Select one of the options to navigate to the page'
    )

if page == 'Home':
    home_page = Home()
    home_page.load_page()

if page == 'Data Cleaning':

    data_cleaning_page = DataCleaning()
    data_cleaning_page.load_page()

if page == 'Data Preprocessing':

    data_preprocessing_page = DataPreprocessing()
    data_preprocessing_page.load_page()

if page == 'Outlier Detection':

    outlier_detection_page = OutlierDetection()
    outlier_detection_page.load_page()

if page == 'Modelling':

    modelling_page = Modeling()
    modelling_page.load_page()

if page == 'Explainable AI':

    explainability_page = Explainability()
    explainability_page.load_page()

if page == 'Visualization':

    visualization_page = Visualization()
    visualization_page.load_page()
