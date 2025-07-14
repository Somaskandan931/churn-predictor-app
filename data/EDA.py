import pandas as pd

# Load the dataset CSV file (update the path if needed)
df = pd.read_csv('C:/Users/somas/PycharmProjects/OnSource_Churn_AI/data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Show the shape of the dataset (rows, columns)
print("Dataset shape:", df.shape)

# Preview the first 5 rows
print(df.head())

# Check data types and null values
print(df.info())

# Count missing values per column
print("\nMissing values per column:")
print(df.isnull().sum())

# Check the distribution of target variable 'Churn'
print("\nTarget variable value counts:")
print(df['Churn'].value_counts())
