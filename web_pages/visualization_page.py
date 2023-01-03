import streamlit as st
from web_pages.page_abstract import Page

COUNT_GRADE_INTEREST_PLOT_PATH = 'images/count_grade_interest_plot.png'
INTEREST_GRADE_PLOT_PATH = 'images/interest_grade_plot.png'
INTEREST_LOAN_PLOT_PATH = 'images/interest_loan_plot.png'
INTEREST_PAIDINTEREST_GRADE_PLOT_PATH = 'images/interest_paidInterest_grade_plot.png'


class Visualization(Page):

    def __init__(self) -> None:
        super().__init__()

    def main(
        self,
        count_grade_interest_plot: str,
        interest_grade_plot: str,
        interest_loan_plot: str,
        interest_paid_interest_grade_plot: str
    ) -> None:
        st.title('Visualizations')

        st.markdown('# Grade - Interest')
        st.image(count_grade_interest_plot)
        st.markdown("""
                    This plot has the grade on the x axis, the count on the left y axis and the interest rate on the right y axis.  
                    We can easily see that the more we advance in the grade the higher the average interest rate. In addition the first 3 grades
                    have the majority of the observations while the last 3 have really few observations.
                    """)

        st.image(interest_grade_plot)
        st.markdown(
            'This classic boxplot further confirms our results from the previous plot and accompanies it perfectly.')

        st.markdown('# Interest - Loan')
        st.image(interest_loan_plot)
        st.markdown("""
                    From this boxplot we can clearly see that there is still differences between the different categories of the loan status and the interest rates.
                    A Late Loan status indicates that the interest rate would be higher on average, as expected, while "charged-off" seems to be having the lowest interest rates.
                    """)

        st.markdown('# Interest Rate - Paid Interest - Grade')
        st.image(interest_paid_interest_grade_plot)
        st.markdown("""
                    In this plot we combine 3 different features. On the x axis we have the paid interest and on the y axis we have the interest rate, that we know are somewhat correlated from our correlation analysis.
                    The datapoints are colored by "Grade". We can easily see that the higher the order of the grade the higher the interest rate, as well as the higher the paid interest, which also makes sense.
                    """)

    def load_page(self) -> None:

        self.main(COUNT_GRADE_INTEREST_PLOT_PATH, INTEREST_GRADE_PLOT_PATH,
                  INTEREST_LOAN_PLOT_PATH, INTEREST_PAIDINTEREST_GRADE_PLOT_PATH)
