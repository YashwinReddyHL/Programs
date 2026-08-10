import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('titanic.csv')


# Colored count plot
sns.countplot(x='Pclass', data=df, palette='Set1')

plt.show()