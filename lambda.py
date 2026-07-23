def sum(a,b):
 return a+b

print(sum(4,5))


def cube(x):
 return x*x*x
print(cube(4))


lambda_cube = lambda y: y*y*y 
print(lambda_cube(5))


sum = lambda a,b:a+b
print(sum(4,5))


add = lambda num: num + 4
print( add(6) ) 


def greater(a,b):
 if a>b:
  return a
 else:
  return b
print(greater(4,5))


Max = lambda a, b : a if(a > b) else b
print(Max(4,5))



my_list= [5,7,2,8,6]
my_list_squared = []
for i in my_list:
 i_squared = i**2
 my_list_squared.append(i_squared)
print(my_list_squared)


my_list_squared = [i**2 for i in my_list]
print(my_list_squared)


my_list_squared = list(map(lambda i: i**2, my_list))
print(my_list_squared)


