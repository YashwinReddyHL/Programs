import numpy as np

def square(number):
    return number*number 
nums = [1,2,3,4]
squared_numbers = list(map(square,nums))
print(squared_numbers)
    

def lamba(nums1):
    list(map(lambda n:n*n,nums1))




from functools import reduce 
def sum_all(a,b):
    return a+b 
nums = [1,2,3,4]
sum = reduce(sum_all,nums)
print(sum)


import numpy as np
a = [1,2,3,4]
sum = np.sum(a)
print("Sum of array elements is",sum)
min = np.min(a)
print("Minimum of array elements is",min)
max = np.max(a)
print("Maximum of array elements is",max)
mean = np.mean(a)
print("Mean of array elements is",mean)
med = np.median(a)
print("Median of array elements is",med)
cor = np.corrcoef(a)
print("Correaltion coefficiant of array elements is",cor)
std = np.std(a)
print("standard deviation of array elements is",std)




def sum(a,b):
 return a+b

print(sum(4,5))
