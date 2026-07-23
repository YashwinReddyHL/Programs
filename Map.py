def add4(x):
    return x+4
list1 = [4,6,7,8,9]

list2 = list(map(add4,list1))
print(list2)


list3 = list(map(lambda x:x+4,list1))
print (list3)


set_of_strings =['abc','def','xyz']
string_map_22 = list(map(lambda my_string: my_string + '_2022', set_of_strings))
print (string_map_22)
