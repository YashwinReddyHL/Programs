import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

card_approval_df = pd.read_csv('credit_dataset.csv')

# clean column names (removes hidden spaces)
card_approval_df.columns = card_approval_df.columns.str.strip()

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
sns.countplot(x='Gender', data=card_approval_df)

plt.subplot(1,2,2)
sns.countplot(x='Ethnicity', data=card_approval_df)

plt.show()