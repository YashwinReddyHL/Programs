import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Load dataset
cars_df = pd.read_csv("cars_data.csv")

# Check columns
print(cars_df.columns)

# Unique values
print("Passengers:", cars_df["Passengers"].unique())
print("Type:", cars_df["Type"].unique())

# Grouped (multi-index)
grouped_simple = cars_df.groupby(["Passengers", "Type"]).size()
print("\nGrouped (multi-index):")
print(grouped_simple)

# Grouped (table format)
grouped_table = cars_df.groupby(["Passengers", "Type"]).size().unstack(fill_value=0)
print("\nGrouped (table format):")
print(grouped_table)

# Grouped (flat table)
grouped_data = cars_df.groupby(["Passengers", "Type"]).size().unstack(fill_value=0).reset_index()
print("\nGrouped (flat table):")
print(grouped_data)

# Plot
grouped_data.plot(
    x="Passengers",
    kind="bar",
    stacked=True,
    colormap=cm.Paired,
    figsize=(10,7)
)

plt.title("Passengers vs Car Type Count", fontsize=16)
plt.xlabel("Passengers")
plt.ylabel("Count")
plt.tight_layout()
plt.show()