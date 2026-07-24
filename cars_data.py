import pandas as pd

cars_df = pd.read_csv("cars_data.csv")

columns = ["Manufacturer","Model","Type","Price","MPG.city","MPG.highway","Horsepower","Rear.seat.room","Passengers"]

print(cars_df[columns].head())