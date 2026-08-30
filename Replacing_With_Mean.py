import pandas as pd

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

# Calculate the mean of Age
mean = titanic_df['age'].mean()
print("Mean age:", mean)

# Replace missing values with the mean
titanic_df['age'] = titanic_df['age'].fillna(mean)

# Display the Age column
print(titanic_df['age'])

# Check remaining missing values
print("Missing age values:", titanic_df['age'].isnull().sum())