def oddeven(x):
 if x%2 == 0:
  return True
 else:
  return False

list1 = [4,5,6,7,8,9]
evenlist = list(filter(oddeven,list1))
print(evenlist)




list1 = [4,5,6,7,8,9]
evenlist = list(filter(lambda x:True if x%2==0 else False,list1))
print(evenlist)
