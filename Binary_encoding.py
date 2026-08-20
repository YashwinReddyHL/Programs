import pandas as pd 

data = pd.DataFrame({
    'Name' : ['A', 'B', 'C', 'D','E'], 
    'Education' : ['High School', 'Masters', 'Doctorate', 'Bachelors','Masters', ]})



education_data = pd.get_dummies(data.Education)
print(education_data)