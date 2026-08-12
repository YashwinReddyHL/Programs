import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("iris.csv")

print(df.columns)

sns.scatterplot(
    x=df.index,
    y=df['sepal width'],
    hue=df['variety'],
    
)

plt.xlabel("Index")
plt.ylabel("Sepal Width")
plt.title("Sepal Width Scatter Plot")

plt.show()