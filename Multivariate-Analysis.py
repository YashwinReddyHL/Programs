import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load credit dataset
card_approval_df = pd.read_csv("credit_dataset.csv")

# Pairplot
sns.pairplot(
    data=card_approval_df[
        ['Age', 'Debt', 'YearsEmployed', 'CreditScore','Income']
    ]
)

plt.show()