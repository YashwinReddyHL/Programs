import pandas as pd
import matplotlib.pyplot as plt

# Load the updated CSV file
df = pd.read_csv("data_out.csv")

# Create histogram for Income
df.Income.hist()

# Display the plot
plt.show()

