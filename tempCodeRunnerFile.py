import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
card_approval_df = pd.read_csv('credit_dataset.csv')

# clean column names (prevents hidden space issues)
card_approval_df.columns = card_approval_df.columns.str.strip()

# correlation matrix
corr_matrix = card_approval_df[['Age','Debt','YearsEmployed','CreditScore','Income']].corr()

# print correlation values
print(corr_matrix)

# visualize correlation
sns.heatmap(corr_matrix, annot=True)
plt.show()