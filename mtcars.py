import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
cars_df = pd.read_csv("cars_data.csv")

# Basic checks
print(cars_df.head())
print("\nColumns:")
print(cars_df.columns)
print("\nData Info:")
print(cars_df.info())

# Frequency of car types
temp = cars_df['Type'].value_counts()
print("\nCar type counts:")
print(temp)

# Plot
temp.plot.bar(figsize=(8,5))

plt.title("Frequency distribution of car types")
plt.xlabel("Car Type")
plt.ylabel("Count")

plt.tight_layout()
plt.show()