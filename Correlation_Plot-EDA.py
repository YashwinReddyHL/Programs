import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('titanic.csv')

# Correlation
print(df.corr(numeric_only=True))

corr = df.corr(numeric_only=True)

sns.heatmap(df.corr(numeric_only=True))
plt.show()
