# this is non color one
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

plt.plot(
    df.index,
    df['sepal width'],
    marker='o'
)

plt.xlabel("Index")
plt.ylabel("Sepal Width")
plt.title("Sepal Width Line Plot")

plt.show()

# This is color one 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("iris.csv")

print(df.columns)

sns.lineplot(
    x=df.index,
    y=df['sepal width'],
    hue=df['variety'],
    
)

plt.xlabel("Index")
plt.ylabel("Sepal Width")
plt.title("Sepal Width Line Plot")

plt.show()


#
