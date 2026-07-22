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


mat = np.array([[1,7,3,4],[3,5,6,8],[10,9,3,4]])
print(mat)
sum = np.sum(mat, axis=1)
print("Sum of array elements row-wise",sum)
sum = np.sum(mat, axis=0)
print("Sum of array elements column-wise",sum)
min = np.min(mat, axis=1)
print("Row-wise minimum of the matrix:",min)
max = np.max(mat,axis=0)
print("Column-wise maximum of the matrix:",max)