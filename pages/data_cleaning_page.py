import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import heatmap
from pandas_profiling import ProfileReport
import pickle
from pages.page_abstract import Page

DATA_PATH = 'util/loans_full_schema.csv'
PANDAS_PROFILE_PATH = 'util/pandas_profile.pkl'
CORRELATION_PLOT_PATH = 'images/correlation_plot.png'


class DataCleaning(Page):

    def __init__(self) -> None:
        super().__init__()

    def load_data(self, data_path: str = DATA_PATH) -> pd.DataFrame:
        df = pd.read_csv(data_path)

        return df

    def load_pandas_profiling(self, pandas_profile_path: str = PANDAS_PROFILE_PATH) -> str:

        with open(pandas_profile_path, 'rb') as fp:
            pandas_profile_html = pickle.load(fp)

        return pandas_profile_html

    def main(self, df: pd.DataFrame, correlation_plot: str = CORRELATION_PLOT_PATH) -> None:

        st.title('Data Cleaning')

        st.markdown('# Important Notes')
        st.markdown("""
                    - We are dealing with a regression problem on tabular data, trying to predict the "interest_rate".
                    - Dataset is not too big (10000, 50) so we can run multiple tests and algorithms without really worrying about complexity
                    - The Business Domain is "Banking", which is a heavily regulated field and requires **Explainability Methods**
                    - Since we are dealing with a regression problem on tabular data, research and experience has shown that decision-tree-based models perform the best. You can refer to this [paper](https://arxiv.org/abs/2207.08815) for more information.
                    """)

        st.markdown('# Data Profiling')
        # This is not working currently
        # st.markdown(self.load_pandas_profiling(
        #     PANDAS_PROFILE_PATH), unsafe_allow_html=True)
        st.markdown("""
                    We use pandas-profiling to quickly navigate through the data, identify problems, see interactions between features and clean the dataset.  
                    After scanning the data we immediately realize that there a lot of problems with our features that need to be fixed in order to analyze them further.  
                    Some interestings points to be made are the following :  
                    - Features with too many missing values
                    - Features that are mostly constant
                    - Highly correlated features
                    - Dataset includes a lot of categorical features
                    - Some have high cardinality  
                    You can navigate to alerts to validate these points
                    """)

        st.markdown('# Clean Dataset')
        st.markdown("""
                    In the process of cleaning the dataset we did a number of steps to deal with the problems mentioned above. Of course due to the limited time, further investigations and experimenting were neglected  
                    As a first step we dropped the features that were :  
                    - Mostly Constant
                    - Had a lot of missing values
                    - Had high cardinality  
                    "verification_income_joint" was a discrete features without too many categories so the missing values could made into a new category called "Missing"
                    """)

        code = """Drop useless columns
        to_drop = [
            'num_accounts_120d_past_due',  # constant
            'emp_title',  # high cardinality (we can fix that)
            'current_accounts_delinq',  # 99% \same
            'num_accounts_30d_past_due',  # 99% \same
            'paid_late_fees',  # 99% \same
            'annual_income_joint',  # 85% missing, continuous, cant be fixed easily
            'debt_to_income_joint',  # 85% missing, continuous, cant be fixed easily
            'months_since_90d_late',  # 75% missing
            'months_since_last_delinq',  # 50% missing
        ]
        df['verification_income_joint'] = df['verification_income_joint'].replace(
            np.nan, 'Missing')  # 85% missing, discrete, can be turned into a new category
        df = df.drop(to_drop, axis=1)"""

        st.code(code, language='python')

        st.markdown('# Correlation')
        # fig, ax = plt.subplots(figsize=(19, 12))
        # heatmap(round(df.corr(), 2), annot=True, ax=ax)
        st.image(correlation_plot)
        st.markdown('After closer inspection, even though these variables have high correlation on certain features, they may actually hold really valueable information and I decided not to drop them. Of course this requires further investigation and testing')

        st.markdown('# Train Validation Test Split')
        st.markdown("""
                    Train test split must be used in order to validate that our model generalizes well.  
                    In addition, we need to create the split before the scaling and the encoding, to have realistic results and simulate real world evaluation
                    """)

        st.markdown('# Feature Engineering')
        st.markdown('Feature engineering actually plays a crucial role in Machine Learning. Unfortunately it takes too much time to familiriaze with the dataset and the Business domain and so was skipped from this project. If more time was given this would be explored thoroughly by combining features and creating new ones')

    def load_page(self) -> None:

        df = self.load_data(DATA_PATH)
        self.main(df, CORRELATION_PLOT_PATH)
