import pandas as pd

# Load the updated CSV file
df = pd.read_csv("data_out.csv")

# Calculate Q1 (25th percentile)
Q1 = df.quantile(0.25, numeric_only=True)

# Calculate Q3 (75th percentile)
Q3 = df.quantile(0.75, numeric_only=True)

# Calculate IQR
IQR = Q3 - Q1

# Display IQR
print(IQR)

# Find outliers
print((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))