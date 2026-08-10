import pandas as pd
import matplotlib.pyplot as plt


# Load the data
df = pd.read_csv('titanic.csv')

#Boxplot
df['Fare'].plot.box()
plt.show()