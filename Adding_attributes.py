 # importing pandas as pd 
import pandas as pd 

# Creating the DataFrame 
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'], 
                   'Event':['Music', 'Poetry', 'Theatre', 'Comedy'], 
                   'Cost':[10000, 5000, 15000, 2000]}) 
# Print the
print (df)


 #using apply function to create a new column
df['Discounted_Price'] = df.apply(lambda row: row.Cost * 0.9, axis = 1)
# Print the DataFrame after addition of new column
print(df)


df = pd.DataFrame({'Name':['John','Ted','Dove','Brad','Rex'], 
                   'Salary':[44000, 35000, 75000, 20000,6000]}) 
# Print the dataframe 
print(df)


# 
def salary_stats(value): 
    if value < 10000: 
        return "very low" 
    elif 10000 <= value < 25000: 
        return "low" 
    elif 25000 <= value < 40000: 
        return "average" 
    elif 40000 <= value < 50000: 
        return "better" 
    elif value >= 50000: 
        return "very good" 
    
df['salary_stats'] = df['Salary'].map(salary_stats) 
print(df)


# 
data = pd.DataFrame({
    'Name' : ['A', 'B', 'C', 'D','E'], 
    'Education' : ['High School', 'Masters', 'Doctorate', 'Bachelors','Masters', ]})
print(data)

