import pandas as pd

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

# Replace missing Age values with the median
titanic_df['age'] = titanic_df['age'].fillna(titanic_df['age'].median())

# Display the Age column
print(titanic_df['age'])

# Check remaining missing values
print("Missing age values:", titanic_df['age'].isnull().sum())