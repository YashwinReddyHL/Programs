import pandas as pd
import numpy as np
import seaborn as sns

# Load the data
df = pd.read_csv('titanic.csv')

# Filter data   
print(df[df['Pclass']==1 ].head())