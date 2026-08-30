import pandas as pd

# Load the updated CSV file
df = pd.read_csv("data_out.csv")

# Calculate skewness of Income
print(df['Income'].skew())

# Display statistical summary of Income
print(df['Income'].describe())