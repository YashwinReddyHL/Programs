import pandas as pd

# Load dataset FIRST
credit_df = pd.read_csv("credit_dataset.csv")

# Now you can use it
credit_df.columns = credit_df.columns.str.strip()

credit_df['Age'] = pd.to_numeric(credit_df['Age'], errors='coerce')
credit_df = credit_df.dropna(subset=['Age'])

q1 = credit_df['Age'].quantile(0.25)
q3 = credit_df['Age'].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

credit_df = credit_df[
    (credit_df['Age'] >= lower_bound) &
    (credit_df['Age'] <= upper_bound)
]

credit_df.info()