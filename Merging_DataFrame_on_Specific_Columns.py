import pandas as pd

dict1 = {
    'ID': [1, 2, 3],
    'Name': ['Pankaj', 'Meghna', 'Lisa'],
    'Country': ['India', 'India', 'USA'],
    'Role': ['CEO', 'CTO', 'CTO']
}

df1 = pd.DataFrame(dict1)

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Pankaj', 'Anupam', 'Amit']
})

print(df1.merge(df2, on='ID'))

print('\n', df1.merge(df2, on='Name'))

