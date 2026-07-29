import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
card_approval_df = pd.read_csv('credit_dataset.csv')

# describe selected columns
print(card_approval_df[['Age','Debt','YearsEmployed','CreditScore','Income']].describe())

# histogram of Age
sns.histplot(card_approval_df['Age'], kde=True)
plt.show()