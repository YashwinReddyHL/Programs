import pandas as pd
import matplotlib.pyplot as plt

cars_df = pd.read_csv("cars_data.csv")

columns = ["Manufacturer","Model","Type","Price","MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]

print(cars_df[columns].head())

# Box plot
cars_df["Price"].plot(kind="box", figsize=(10,7))

plt.title("Box Plot of Car Prices")
plt.ylabel("Price")

plt.show()