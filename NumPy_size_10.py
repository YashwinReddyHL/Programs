import numpy as np

x = np.zeros(10)
print(x)
print("Update sixth value to 11")
x[6] = 11
print(x)


item_list = ['Bread', 'Milk', 'Eggs', 'Butter', 'Cocoa']
student_marks = [78, 47, 96, 55, 34]
hetero_list =  [ 1,2,3.0, 'text', True, 3+2j ]
student_marks = [78, 47, 96, 55, 34]
for i in range(len(student_marks)):
    student_marks[i]+=5
print(student_marks)


list1 = list(range(1,1000000))
list2 = list(range(2,1000001))
list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])


import numpy as np
student_marks_arr = np.array([78, 92, 36, 64, 89])
print(student_marks_arr)

car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 302 ,309]]
car_attributes_arr = np.array(car_attributes)
print(car_attributes_arr)


print(car_attributes_arr.shape)


print ( car_attributes_arr.dtype)


car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 302 ,309]]
car_attributes_arr = np.array(car_attributes, dtype = 'float')
print(car_attributes_arr)
print(car_attributes_arr.dtype)