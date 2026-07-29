import pandas as pd
import numpy as np

credit_df = pd.read_csv("credit_dataset.csv")

credit_df['Age'] = pd.to_numeric(credit_df['Age'], errors='coerce')

lower_bound = credit_df['Age'].quantile(0.25)
upper_bound = credit_df['Age'].quantile(0.75)

m = credit_df['Age'].mean()
print('mean:', m)

credit_df.loc[
    (credit_df['Age'] < lower_bound) | (credit_df['Age'] > upper_bound),'Age'] = m