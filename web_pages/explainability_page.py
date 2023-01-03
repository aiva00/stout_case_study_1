import streamlit as st
import pickle
import shap
from web_pages.page_abstract import Page

SHAP_VALUES_PATH = 'util/shap_values.pkl'
SHAP_FORCE_PLOT_PATH = 'images/shap_force_plot.png'
SHAP_SUMMARY_PLOT_BAR_PATH = 'images/shap_summary_plot_bar.png'
SHAP_SUMMARY_PLOT_VIOLING_PATH = 'images/shap_summary_plot_violin.png'
FEATURE_IMPORTANCE_RF_PATH = 'images/feature_importance_rf_plot.png'
FEATURE_IMPORTANCE_RIDGE_PATH = 'images/feature_importance_ridge_plot.png'


class Explainability(Page):

    def __init__(self) -> None:
        super().__init__()

    # def load_shap_values(self, shap_values_path: str = SHAP_VALUES_PATH) -> None:

    #     with open(shap_values_path, 'rb') as fp:
    #         shap_values = pickle.load(fp)
    #     return shap_values

    def main(
            self,
            feature_importance_rf: str,
            feature_importance_ridge: str,
            shap_summary_plot_bar: str,
            shap_summary_plot_violin: str,
            shap_force_plot: str
    ) -> None:

        st.title('XAI : Explainable AI')

        st.markdown("""
                    Explainable AI is an integral part of Machine Learning altought it is currently not leveraged as much as it should be. Considering that we are working in a
                    highly regulated domain, banking, it is essential that we can provide the end users with explanations about our model's decisions. Another important reason
                    why Explainable AI is beneficial is that it enables the people working on the model to understand it better, identify problems and make it more trustworthy.
                    """)

        st.markdown('# Feature Importance of Random Forest with std\'s')

        st.image(feature_importance_rf)
        st.markdown('We can clearly see that a lot of feature don\'t really play an important role in the model. Grade is by far the best feature. Another interesting point is that the outlier score seems to have an impact when needed')

        st.markdown('# Weights of Ridge Model')

        st.image(feature_importance_ridge)

        st.markdown('# SHAP values')

        st.markdown('Summary Plot:')

        st.image(shap_summary_plot_bar)
        st.markdown(
            'From these plot we can see which features really affect the output of the model')

        st.markdown('Summary Violin Plot:')
        st.image(shap_summary_plot_violin)
        st.markdown(
            'From this plot we can also see how higher or lower values affect the model output')

        st.markdown(
            'Explanation of the decision of the model for a single sample:')
        st.image(shap_force_plot)
        st.markdown('We can identify that the grade variable drives the interest rate to go lower, while being assisted by the sub_grade. This plot refers to a single random observation.')

    def load_page(self):

        self.main(FEATURE_IMPORTANCE_RF_PATH, FEATURE_IMPORTANCE_RIDGE_PATH,
                  SHAP_SUMMARY_PLOT_BAR_PATH, SHAP_SUMMARY_PLOT_VIOLING_PATH, SHAP_FORCE_PLOT_PATH)


# def st_shap(plot, height=None) -> None:
#     shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
#     st.components.v1.html(shap_html, height=height)
