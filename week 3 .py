'''
# 1
def square(number):
    return number*number
nums = [1,2,3,4]
squared_numbers = list(map(square,nums)) 
print (squared_numbers)

nums1 = [1,2,3,4,5,6]
sqareOfnums1 = list(map(lambda n:n*n,nums1)) 
print (sqareOfnums1)


# 2
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
nums = [1,2,3,4]
evens = list(filter(is_even,nums))
print (evens)


# 3
from functools import reduce 
def sum_all (a,b):
    return a + b 
nums = [1,2,3,4]
sum = reduce(sum_all,nums)
print (sum)


# 4
nums = [1,2,3,4]
evens = list(filter(lambda n:n%2==0 , nums))
print (evens)


# 5
import pandas as pd
lst = ['Apple','Mango','Banana''Pine Apple','Grapes', 'Watermelon']
df = pd.DataFrame(lst)
print (df)

# 6
import pandas as pd
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
df = pd.DataFrame(data)
print(df)


# 7
import pandas as pd

df = pd.read_csv('student.csv',sep='\t')
print(df)


# 8
import pandas as pd

df = pd.read_csv('student.csv',sep='\t',usecols=["REG-NO","SEM"])
print(df)


# 9
import pandas as pd  
d1 = {"Name": ["Pankaj", "Lisa", "David"], "ID": [1, 2, 3], "Role": ["CEO", "Editor","Author"]}  
df =pd.DataFrame(d1)  
print(df)  
df_melted = pd.melt(df, id_vars=["ID"], value_vars=["Name","Role"])  
print(df_melted)  


# 10
import pandas as pd    
df = pd.DataFrame({'A': ['John', 'Boby', 'Mina'],'B': ['Masters', 'Graduate', 'Graduate'],'C': [27, 23, 21]})
print(df)  
'''

# 11
