import pandas as pd
import matplotlib.pyplot as plt

cars_df = pd.read_csv("cars_data.csv")

# Aggregate properly (bar charts need grouped data)
grouped = cars_df.groupby("Type")["MPG.city"].mean()

plt.figure(figsize=(10,7))
plt.barh(grouped.index, grouped.values, height=0.5, label="Avg Mileage in City")

plt.title("Type vs MPG.city")
plt.xlabel("MPG.city")
plt.ylabel("Type")
plt.legend()

plt.show()