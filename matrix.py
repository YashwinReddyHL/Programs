import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x)


x=np.zeros(10)
print(x)
print("update sixth value 11")
x[6]=11
print(x)

item_list=['bread','milk','eggs']
student_marks=[23,44,32]
hetero_list=[1,2,3.0,'text',True,3+2j]
print(student_marks)
print(item_list)
print(hetero_list)

student_marks=[23,44,32]
for i in range(len(student_marks)):
    student_marks[i]+=5
print(student_marks)
  
import numpy as np
student_marks_arr=np.array([34,55,32,56,76])
print(student_marks_arr)


#vectorize operations
arr = np.array([1,2,3,4,5])
result = arr*2
print(result)

a=np.array([1,2,3])
b=np.array([5,6,7])
result=np.dot(a,b)
print(result)

a=np.array([1,2])
b=np.array([5,6])
result=np.outer(a,b)
print(result)

#element wise 
a=np.array([1,2,4])
b=np.array([5,6,6])
result=np.multiply(a,b)
print(result)

#array addition
a=np.array([1,2,4])
b=np.array([5,6,6])
result=a+b
print(result)

#slicing
foods=np.array(['biriyani','dosa','palav','egg rice','sambar'])
print(foods[1:4])

#2d slicing
foods=np.array(['biriyani','dosa','palav','egg rice','sambar'])
numbers=np.array([32,43,13,56,87,46])
phone=np.array([97,54,34,98,66])
k_fo_nu_ph=np.array([foods,numbers,phone],dtype=object)
print(k_fo_nu_ph[0:3])






















