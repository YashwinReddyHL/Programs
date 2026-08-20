import pandas as pd

d1 = {
    'Name': ['Pankaj', 'Meghna', 'Lisa'],
    'Country': ['India', 'India', 'USA']
}

# DataFrame 1
df1 = pd.DataFrame(d1)
print('DataFrame 1:\n', df1, '\n')


# DataFrame 2
df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Pankaj', 'Anupam', 'Amit']
})

print('DataFrame 2:\n', df2, '\n')


# DataFrame 3
df3 = pd.DataFrame({
    'Name': ['Priya'],
    'Country': ['India'],
    'Role': ['COO']
})

print('DataFrame 3:\n', df3, '\n')

# 
same_cols_df = pd.concat([df1,df3],ignore_index=True)
print(same_cols_df)

#
a_df = pd.concat([df1, df2], ignore_index=True)
print(a_df)

# 
c_df = pd.concat([df1,df2],ignore_index=True)
print(c_df)