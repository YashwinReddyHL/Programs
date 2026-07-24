import pandas as pd
import matplotlib.pyplot as plt

# Load data
cars_df = pd.read_csv("cars_data.csv")

# Scatter plot
ax = cars_df.plot(
    x="Horsepower",
    y="MPG.city",
    kind="scatter",
    color="black",
    marker="*",
    figsize=(10,7)
)

# Labels and title
ax.set_xlabel("Horsepower")
ax.set_ylabel("MPG.city")
ax.set_title("Horsepower vs MPG.city", fontsize=16)

plt.show()