import pandas as pd

d1 = {
    'Name': ['Pankaj', 'Meghna', 'Lisa'],
    'Country': ['India', 'India', 'USA']
}

# DataFrame 1
df1 = pd.DataFrame(d1)


# DataFrame 2
df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Pankaj', 'Anupam', 'Amit']
})


# Left, Right, and Outer Join 
print('Result Left Join:\n', df1.merge(df2, how='left'))
print('Result Right Join:\n', df1.merge(df2, how='right'))
print('Result Outer Join:\n', df1.merge(df2, how='outer'))