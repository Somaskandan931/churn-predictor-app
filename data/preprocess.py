import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv('C:/Users/somas/PycharmProjects/OnSource_Churn_AI/data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Drop customerID column (unique identifier, not useful for modeling)
df = df.drop('customerID', axis=1)

# Convert TotalCharges to numeric (it has some empty strings)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Fill missing TotalCharges with median
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

# Convert target variable 'Churn' to binary
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Separate features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Identify categorical and numerical columns
cat_cols = X.select_dtypes(include=['object']).columns
num_cols = X.select_dtypes(include=['int64', 'float64']).columns

# One-hot encode categorical variables
X_encoded = pd.get_dummies(X, columns=cat_cols)

print(f"Original features: {X.shape[1]} columns")
print(f"Features after encoding: {X_encoded.shape[1]} columns")

# Split data into train and test sets (stratify on target)
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42, stratify=y)

print(f"Train set shape: {X_train.shape}")
print(f"Test set shape: {X_test.shape}")

# Create processed data folder if it doesn't exist
processed_data_dir = 'C:/Users/somas/PycharmProjects/OnSource_Churn_AI/data/processed'
os.makedirs(processed_data_dir, exist_ok=True)

# Combine features and target for train and test sets
train_df = pd.concat([X_train.reset_index(drop=True), y_train.reset_index(drop=True)], axis=1)
test_df = pd.concat([X_test.reset_index(drop=True), y_test.reset_index(drop=True)], axis=1)

# Save to CSV files
train_df.to_csv(os.path.join(processed_data_dir, 'train_set.csv'), index=False)
test_df.to_csv(os.path.join(processed_data_dir, 'test_set.csv'), index=False)

print(f"✅ Processed train and test datasets saved to '{processed_data_dir}'")
