import pandas as pd
import matplotlib.pyplot as plt

# Load data
cars_df = pd.read_csv("cars_data.csv")

# Create subplots
fig, ax = plt.subplots(2, 3)
fig.set_figwidth(10)
fig.set_figheight(7)
fig.suptitle("Multiple Box Plots", fontsize=16)

types = ["Compact", "Large", "Midsize", "Small", "Sporty", "Van"]

for i, car_type in enumerate(types):
    row = i // 3
    col = i % 3
    
    data = cars_df[cars_df["Type"] == car_type]["Price"]
    
    if not data.empty:
        ax[row][col].boxplot(data)
    else:
        ax[row][col].text(0.5, 0.5, "No Data", ha='center')
    
    ax[row][col].set_title(car_type)

fig.tight_layout()
plt.show()