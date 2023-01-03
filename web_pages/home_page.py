import streamlit as st
from web_pages.page_abstract import Page

STOUT_IMAGE = 'images/stout_logo.png'


class Home(Page):

    def __init__(self) -> None:
        super().__init__()

    def main(self, stout_image_path: str = STOUT_IMAGE) -> None:

        st.image(stout_image_path)
        st.title('Welcome to the "Loans" project (Case Study 1)')

        st.markdown("""
                    This project was made by [Christos Aivazidis](https://www.linkedin.com/in/aiva00) as part of the Stout\'s Case Study 1  
                      
                    Use the navigation bar on the left to navigate to the various pages and explore the project steps I took to bring it to life.  
                    """)

        st.markdown("""
                    In this case study we analyze the loans dataset and there are 2 important goals:  
                    1. Analyze the dataset properly (cleaning, modelling etc.)
                    2. Create some interesting visualizations
                    """)

        st.markdown(
            'You can also check the jupyter notebook for a detailed step-by-step of the process')

        st.info('Due to the limited time the webapp is not really \'flashy\' and more work could definitely be put into it but I chose to focus more on the Analysis that I think matters the most.')

    def load_page(self) -> None:

        self.main(STOUT_IMAGE)
