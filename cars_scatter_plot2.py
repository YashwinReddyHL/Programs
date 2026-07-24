import pandas as pd
import matplotlib.pyplot as plt

# Load data
cars_df = pd.read_csv("cars_data.csv")

# Create figure
fig = plt.figure()
fig.set_figwidth(10)
fig.set_figheight(7)

# Get unique car types
car_type_list = cars_df["Type"].unique()
print(car_type_list)

colors_list = ['red','blue','pink','green','black','yellow']

# Loop through each type
for car_type, colr in zip(car_type_list, colors_list):
    x = cars_df[cars_df["Type"] == car_type]["Horsepower"]
    y = cars_df[cars_df["Type"] == car_type]["MPG.city"]
    plt.scatter(x, y, color=colr, label=car_type)

# Labels and title
plt.suptitle("Scatter plot of horsepower and mileage", fontsize=16)
plt.xlabel("Horsepower")
plt.ylabel("Mileage City")
plt.legend()

plt.show()