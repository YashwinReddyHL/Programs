import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load credit dataset
card_approval_df = pd.read_csv("credit_dataset.csv")

# Pairplot with 2 colors
sns.pairplot(
    data=card_approval_df,
    vars=['Age', 'Debt', 'YearsEmployed', 'CreditScore', 'Income'],
    hue='Approved'
)

plt.show()