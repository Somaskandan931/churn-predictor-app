import pandas as pd

def preprocess_input(data, train_columns):
    """
    Preprocess a single input instance (dict) to match training pipeline.

    Args:
        data (dict): Raw input dictionary (JSON from frontend)
        train_columns (list): List of columns the model was trained with

    Returns:
        pd.DataFrame: One-hot encoded and aligned DataFrame with model features
    """
    input_df = pd.DataFrame([data])

    # Ensure TotalCharges is numeric
    input_df['TotalCharges'] = pd.to_numeric(input_df.get('TotalCharges', 0), errors='coerce')

    # Avoid chained assignment warning by assigning explicitly
    median_total = input_df['TotalCharges'].median()
    input_df['TotalCharges'] = input_df['TotalCharges'].fillna(median_total)

    # One-hot encode categorical columns
    input_encoded = pd.get_dummies(input_df)

    # Reindex to match training features
    input_encoded = input_encoded.reindex(columns=train_columns, fill_value=0)

    return input_encoded
