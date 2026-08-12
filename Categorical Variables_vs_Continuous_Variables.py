import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
card_approval_df = pd.read_csv("credit_dataset.csv")

# Check the data
print(card_approval_df.head())

# Mean values by Approved
print(
    card_approval_df.groupby('Approved')
    .mean(numeric_only=True)[['Age', 'Debt', 'YearsEmployed']]
)

# KDE plot
plt.figure(figsize=(5, 4))

sns.kdeplot(
    data=card_approval_df,
    x='Age',
    hue='Approved',
    fill=True
)

plt.title("Age Distribution by Approval")
plt.xlabel("Age")
plt.ylabel("Density")

plt.show()

# this is another count plot graph 
sns.countplot(
    data=card_approval_df,
    x='Approved',
    hue='Gender'
)

plt.title("Approval Status by Gender")
plt.xlabel("Approved")
plt.ylabel("Count")

plt.show()
