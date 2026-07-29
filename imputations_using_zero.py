import pandas as pd

# 1. Load file
try:
    credit_df = pd.read_csv("credit_dataset.csv")
    print("File loaded")
except Exception as e:
    print("File error:", e)

# 2. Check dataframe
print("Type:", type(credit_df))
print("Columns:", credit_df.columns)

# 3. Fix column name if needed
if 'Age' not in credit_df.columns:
    print("Fixing column name...")
    credit_df.columns = credit_df.columns.str.strip().str.capitalize()

print("Columns after fix:", credit_df.columns)

# 4. Convert to numeric
credit_df['Age'] = pd.to_numeric(credit_df['Age'], errors='coerce')

# 5. Check data
print(credit_df['Age'].head())
print("Null values:", credit_df['Age'].isnull().sum())

# 6. Bounds
Q1 = credit_df['Age'].quantile(0.25)
Q3 = credit_df['Age'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Bounds:", lower_bound, upper_bound)

# 7. Replace outliers
credit_df.loc[
    (credit_df['Age'] < lower_bound) | (credit_df['Age'] > upper_bound),
    'Age'
] = 0

print("Final done")

