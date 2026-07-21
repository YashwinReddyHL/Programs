# import pandas as pd
# lit = ['Apple','Mango','Banana','PineApple','Grapes','Watermelon']
# df = pd.DataFrame(lit)
# print(df)



import pandas as pd
 
df = pd.read_csv("student.csv",sep="\t",usecols=["REG-NO","SEM"])
# df_reversed = df.iloc[::-1]
print(df)

import pandas as pd

d1 = {"Name": ["Pankaj", "Lisa", "David"], "ID": [1, 2, 3], "Role": ["CEO", "Editor","Author"]}  
df =pd.DataFrame(d1)  
print(df)  
df_melted = pd.melt(df, id_vars=["ID"], value_vars=["Name","Role"])  
print(df_melted)


import pandas as pd    
df = pd.DataFrame({'A': ['John', 'Boby', 'Mina'],'B': ['Masters', 'Graduate', 'Graduate'],'C': [27, 23, 21]})
print(df)


import numpy as np
x = np.arange (2,11).reshape(3,3)
print (x)

import numpy as np
x = np.zeros(10)
print (x)
print("Update sixth value to 11")
x[6] = 11
print (x)


item_list = ['Bread', 'Milk', 'Eggs', 'Butter', 'Cocoa']
student_marks = [78, 47, 96, 55, 34]
hetero_list =  [ 1,2,3.0, 'text', True, 3+2j ]
student_marks = [78, 47, 96, 55, 34]
for i in range(len(student_marks)):
    student_marks[i]+=5
print(student_marks)


