import streamlit as st
import pickle
from web_pages.page_abstract import Page

AUTO_ML_RESULTS_PATH = 'images/auto_ml_plot.png'
RF_METRICS_TABLE_PATH = 'util/rf_metrics_table.pkl'
RIDGE_METRICS_TABLE_PATH = 'util/ridge_metrics_table.pkl'


class Modeling(Page):

    def __init__(self) -> None:
        super().__init__()

    def load_metrics_tables(self, rf_metrics_table_path: str = RF_METRICS_TABLE_PATH, ridge_metrics_table_path: str = RIDGE_METRICS_TABLE_PATH):

        with open(rf_metrics_table_path, 'rb') as fp:
            rf_metrics_table = pickle.load(fp)

        with open(ridge_metrics_table_path, 'rb') as fp:
            ridge_metrics_table = pickle.load(fp)
        return rf_metrics_table, ridge_metrics_table

    def main(
        self,
        auto_ml_results: str = AUTO_ML_RESULTS_PATH,
        rf_metrics_table=RF_METRICS_TABLE_PATH,
        ridge_metrics_table=RIDGE_METRICS_TABLE_PATH
    ) -> None:

        rf_metrics_table, ridge_metrics_table = self.load_metrics_tables(
            rf_metrics_table, ridge_metrics_table)

        st.title('Modelling (Regression)')

        st.markdown("""
                    The machine learning algorithm that needs to be used in each case highly depends on the goal of the project. Some key things that need to be taken into account are:  
                    - Accuracy(Do we need to optimize how good the model is?)
                    - Inference Speed(Do we need to have really fast predictions)
                    - Training time(Do we have limited resources and we don’t want to train neural networks for months?)
                    - Complexity(Do we need a really small model to operate on an embedded system?)
                    - Explainability(Do we need an explainable model because the field or the client requires full transparency?)
                    """)

        st.markdown('# AutoML')
        st.markdown(
            'AutoML was used in order to test multiple models and their potency with low-code.')
        st.image(auto_ml_results)
        st.markdown("""
                    Decision-tree-based models (LGB, RF) are top performers as expected, but the Bayesian Ridge model seems to be pefroming exceptionally well.  
                    The Random Forest and the Bayesian Ridge model will be further tested.  
                      
                    The metrics seem really promising which may indicate data leakage. (This is a problem that requires a lot of time to be fixed)
                    """)

        st.markdown('# Random Forest Regressor')
        st.table(rf_metrics_table)

        st.markdown('# Hyperparameter Tuning using HyperOpt')
        st.markdown("""
                    Hyperopt and the TPE algorithm were used to find the optimal set of hyperpameters only by defining the search space.  
                    You can see which hyperpameters were tweaked and the search space in the code below:
                    """)
        code = """
        def objective(search_space):
            model = RandomForestRegressor(
                **search_space,
                random_state=RANDOM_STATE,
                n_jobs=N_JOBS
            )
            model.fit(x_train, y_train)
            y_pred_val = model.predict(x_val)
            mse = mean_squared_error(y_val, y_pred_val)
            return {'loss': mse, 'status': STATUS_OK}

        search_space={
            'n_estimators':hp.randint('n_estimators',200,1000),
            'max_depth': hp.randint('max_depth',10,200),                   
            'min_samples_split':hp.uniform('min_samples_split',0,1),   
            'min_samples_leaf':hp.randint('min_samples_leaf',1,10),          
            'criterion':hp.choice('criterion',['mse','mae']),
            'max_features':hp.choice('max_features',['sqrt', 'log2'])
        }
        algorithm = tpe.suggest

        best_params = fmin(
        fn=objective,
        space=search_space,
        algo=algorithm,
        rstate=RANDOM_STATE,
        max_evals=200)
        print(best_params)
        """
        st.code(code, language='python')
        st.markdown("""
                    Unfortunately the search didn't yield great results and that is because the Parameter Space wasn't carefully selected.
                    With more time this could be further investigated.
                    """)

        st.markdown('# Final Model')
        st.markdown("""
                    As a final model we chose the Random Forest Regressor with default parameters as they showed the best results in the metrics.
                    The tuned model was underperforming and wasn't eventually used
                    """)

        # Add that at this point you can already navigate to "Explanation" to see model explanation

        st.markdown('# Bayesian Ridge Model')
        st.markdown("""
                    This model seemed quite promising from the AutoML, but further testing proved that it wasn't that good after all.  
                    Below you can find the metrics of the model. A Feature importance plot can be found in the Explainability tab
                    """)
        st.table(ridge_metrics_table)

        # Add explanation
    def load_page(self) -> None:

        self.main(AUTO_ML_RESULTS_PATH,
                  RF_METRICS_TABLE_PATH, RIDGE_METRICS_TABLE_PATH)
