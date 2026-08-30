import pandas as pd

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

# Display unique values in the deck column
print("Unique values before replacing missing values:")
print(titanic_df['deck'].unique())

# Replace missing values with an arbitrary value
titanic_df['deck'] = titanic_df['deck'].fillna('C')

# Check missing values after replacement
print("\nMissing values after replacement:")
print(titanic_df['deck'].isnull().sum())

# Display the updated DataFrame
print("\nUpdated Titanic DataFrame:")
print(titanic_df)