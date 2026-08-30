import pandas as pd

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

# Count missing values in each column
print(titanic_df.isnull().sum())

# Remove rows containing missing values
df = titanic_df.dropna(axis=0)

# Count missing values after removing rows
print(df.isnull().sum())