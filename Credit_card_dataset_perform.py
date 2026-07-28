import pandas as pd
import matplotlib.pyplot as plt

credit_df = pd.read_csv("credit_dataset.csv")

# Clean column names
credit_df.columns = credit_df.columns.str.strip()

# Print columns to verify
print(credit_df.columns)

# Convert to numeric safely
if 'Age' in credit_df.columns:
    credit_df['Age'] = pd.to_numeric(credit_df['Age'], errors='coerce')

if 'Debt' in credit_df.columns:
    credit_df['Debt'] = pd.to_numeric(credit_df['Debt'], errors='coerce')

# ---- Box plot (Age) ----
if 'Age' in credit_df.columns:
    credit_df['Age'].dropna().plot(kind='box', title='Age Box Plot')
    plt.show()
else:
    print("Column 'Age' not found")

# ---- Histogram (Debt) ----
if 'Debt' in credit_df.columns:
    credit_df['Debt'].dropna().plot(kind='hist', bins=20, title='Debt Distribution')
    plt.show()
else:
    print("Column 'Debt' not found")