import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")

# Display first 5 rows
print(titanic_df.head())

# Display missing values count
print(titanic_df.isnull().sum())

# Bar chart of missing values
msno.bar(titanic_df)
plt.show()

# Matrix of missing values
msno.matrix(titanic_df)
plt.show()