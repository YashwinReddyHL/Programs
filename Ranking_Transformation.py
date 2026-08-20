import pandas as pd 

data = pd.DataFrame({
    'Name' : ['A', 'B', 'C', 'D','E'], 
    'Education' : ['High School', 'Masters', 'Doctorate', 'Bachelors','Masters', ]})

education_map = {
'High School' : 1,
'Bachelors' : 2,
'Masters': 3,
'Doctorate': 4
}
education_data = data['Education'].map(education_map)
data['Education'] = education_data
print(data)


education_map = {
    'High School' : 12,
    'Bachelors' : 16,
    'Masters': 18,
    'Doctorate': 21
}
education_data = data['Education'].map(education_map)
data['Education'] = education_data
print(data)