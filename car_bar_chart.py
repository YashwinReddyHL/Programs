import pandas as pd
import matplotlib.pyplot as plt

cars_df = pd.read_csv("cars_data.csv")

grouped = cars_df.groupby("Type")["MPG.city"].mean()

plt.figure(figsize=(10,7))
plt.bar(grouped.index, grouped.values)

plt.title("Car Type vs Avg MPG.city")
plt.xlabel("Type")
plt.ylabel("MPG.city")

plt.show()