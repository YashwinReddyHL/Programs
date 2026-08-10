import pandas as pd
import numpy as np
import seaborn as sns

# Load the data
df = pd.read_csv('titanic.csv')

#Find null values   
print(df.isnull().sum())

# # clear and shorted 
# print(df.isnull().sum().sort_values(ascending=False))