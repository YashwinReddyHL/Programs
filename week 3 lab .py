'''
#
def sum(a,b):
    return a+b
print(sum(4,5))


#
def cube (x):
    return x*x*x
print(cube(4))
lambda_cube = lambda y : y*y*y
print(lambda_cube(5))


#
sum = lambda a,b:a+b
print(sum(4,5))


#
import numpy as np
x = np.arange (2,11).reshape(3,3)
print (x)


#
import numpy as np
x = np.zeros(10)
print (x)
print("Update sixth value to 11")
x[6] = 11
print (x)


#
item_list = ['Bread', 'Milk', 'Eggs', 'Butter', 'Cocoa']
student_marks = [78, 47, 96, 55, 34]
hetero_list =  [ 1,2,3.0, 'text', True, 3+2j ]
student_marks = [78, 47, 96, 55, 34]
for i in range(len(student_marks)):
    student_marks[i]+=5
print(student_marks)


#
list1 = list(range(1,1000000))
list2 = list(range(2,1000001))
list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])

#
import numpy as np
horsepower = [130, 165, 150, 150, 140]
horsepower_arr = np.array(horsepower)
print("Mean horsepower = ",np.mean(horsepower_arr))
print("Minimum horsepower: ", np.min(horsepower_arr))
print("Maximum horsepower: ", np.max(horsepower_arr))


#
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.dot(a, b)
print(result)


#
import numpy as np
a = np.array([1, 2])
b = np.array([3, 4])
result = np.outer(a, b)
print(result)


#
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.multiply(a, b)
print(result)


#
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a + b
print(result)


#
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a + b
print(result)


#
import numpy as np
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
result = a @ b
print(result)
'''

#
