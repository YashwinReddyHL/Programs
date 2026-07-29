import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

# load dataset
card_approval_df = pd.read_csv('credit_dataset.csv')

# preview data
print(card_approval_df.head())

# dataset info
card_approval_df.info()


# check duplicate rows
duplicates = card_approval_df.duplicated().sum()
print("Duplicate rows:", duplicates)

# duplicate count (your exact line)
print(card_approval_df.duplicated().sum())
