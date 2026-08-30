import pandas as pd

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

# Display column names
print(titanic_df.columns)

# Remove the deck column
df = titanic_df.drop(['deck'], axis=1)

# Count missing values after removing the deck column
print(df.isnull().sum())