import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
cars_df = pd.read_csv("cars_data.csv")

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.set_figwidth(10)
fig.set_figheight(7)

# Boxplots
ax1.boxplot(cars_df["Horsepower"])
ax2.boxplot(cars_df["MPG.city"])

# Titles and labels
ax1.set_title('Horsepower')
ax1.set_xlabel('Horsepower')

ax2.set_title('City Mileage')
ax2.set_xlabel("City Mileage (in miles per US gallon)")

# Layout and display
fig.tight_layout()
plt.show()