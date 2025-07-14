import shap
import pandas as pd

class ExplainabilityHelper:
    def __init__(self, model):
        self.explainer = shap.TreeExplainer(model)

    def get_shap_explanation(self, input_df, top_n=5):
        """
        Compute SHAP values for a single prediction input and return top features.

        Args:
            input_df (pd.DataFrame): One preprocessed row of input data.
            top_n (int): Number of top impacting features to return.

        Returns:
            List[Dict[str, float]]: List of top_n features and their SHAP values.
        """
        shap_values = self.explainer.shap_values(input_df)
        shap_val_row = shap_values[0]  # Only one row expected

        feature_impacts = dict(zip(input_df.columns, shap_val_row))
        top_features = sorted(feature_impacts.items(), key=lambda x: abs(x[1]), reverse=True)[:top_n]

        return [{'feature': k, 'impact': round(v, 4)} for k, v in top_features]
