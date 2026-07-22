import pandas as pd
import matplotlib.pyplot as plt

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")

data = wine_reviews["points"].value_counts()

plt.bar(data.index, data.values)

plt.title("Wine Review Scores")
plt.xlabel("Points")
plt.ylabel("Frequency")

plt.show()