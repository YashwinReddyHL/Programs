import numpy as np
mat=np.array([[1,2,3,4][5,3,4,6][5,6,7,8]])
print(mat)
sum=np.sum(mat,axis=1)
print("sum of array elements row-wise",sum)
sum=np.sum(mat,axis=0)
print("sum of array elemets colume-wise",sum)
min=np.min(mat,axis=1)
print("row-wise minimum of the matrix:",min)
max=np.max(mat,axis=0)
print("colume-wise maximun of the matrix:",max)



