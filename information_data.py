import pandas as pd
import numpy as np
import seaborn as sns

# Load the data
df = pd.read_csv('titanic.csv')

# Basic information
df.info()

# Describe the data
print(df.describe())
