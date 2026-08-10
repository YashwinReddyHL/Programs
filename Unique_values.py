import pandas as pd
import numpy as np
import seaborn as sns

# Load the data
df = pd.read_csv('titanic.csv')

# Unique values
print(df['Pclass'].unique())
print(df['Survived'].unique())
print(df['Sex'].unique())