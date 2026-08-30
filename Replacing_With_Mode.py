import pandas as pd

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

# Find the mode of the deck column
mode = titanic_df['deck'].mode()[0]
print("Mode:", mode)

# Replace missing values with the mode
titanic_df['deck'] = titanic_df['deck'].fillna(mode)

# Display the deck column
print(titanic_df['deck'])

# Check remaining missing values
print("Missing deck values:", titanic_df['deck'].isnull().sum())