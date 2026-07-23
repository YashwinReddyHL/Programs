from functools import reduce
def sum(x,y):
    return x+y
list1 = [6,7,8,9]
s = reduce(sum,list1)
print(s)