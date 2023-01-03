import streamlit as st
from web_pages.page_abstract import Page

OUTLIER_IMAGE_PATH = 'images/explain_outlier_plot.png'


class OutlierDetection(Page):

    def __init__(self) -> None:
        super().__init__()

    def main(self, outlier_image: str = OUTLIER_IMAGE_PATH) -> None:

        st.title('Outlier Detection')

        st.markdown("""
                    Outlier detection plays a really important role in Machine Learning and can help improve the performance of 
                    a Regression Model greatly. In order to be effective though one has to consider many aspects, such as why 
                    some features take extreme values and if it is normal, so as to determine if the observations are worth dropping. 
                    With this limited time we can't really investigate further so we will just incorporate the outlier scores for now and 
                    give an explanation on a random sample of an outlier. Isolation Forest and KNN outlier detection were also tried, but we
                    ended up using ECOD to have a beautiful explanation of outliers.
                    """)

        st.markdown('## ECOD')
        st.markdown("""
                    ECOD first estimates the underlying distribution of the input data in a nonparametric fashion by computing 
                    the empirical cumulative distribution per dimension of the data. ECOD then uses these empirical distributions 
                    to estimate tail probabilities per dimension for each data point.
                    """)

        st.image(outlier_image)
        st.markdown("""
                 In the image above we can see that certain features differ greatly from their "normal" distributions
                 """)

    def load_page(self) -> None:
        self.main(OUTLIER_IMAGE_PATH)
