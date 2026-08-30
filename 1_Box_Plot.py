import pandas as pd
import matplotlib.pyplot as plt

# Load the updated CSV file
df = pd.read_csv("data_out.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Display column names
print(df.columns.tolist())

# Create box plot for Loan_amount
plt.boxplot(df["Loan_amount"])

# Display the plot
plt.title("Loan Amount")
plt.ylabel("Loan Amount")
plt.show()

# Create box plots of Loan_amount grouped by approval_status
df.boxplot(column="Loan_amount", by="Approval_status")

# Set title
plt.title("Loan Amount by Approval Status")
plt.suptitle("")

# Display the plot
plt.show()