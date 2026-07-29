import pandas as pd
import numpy as np

credit_df = pd.read_csv("credit_dataset.csv")

# ensure numeric
credit_df['Age'] = pd.to_numeric(credit_df['Age'], errors='coerce')

# calculate IQR
Q1 = credit_df['Age'].quantile(0.25)
Q3 = credit_df['Age'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# median
m = credit_df['Age'].median()
print("median:", m)

# replace outliers
credit_df.loc[
    (credit_df['Age'] < lower_bound) | (credit_df['Age'] > upper_bound),
    'Age'
] = m
