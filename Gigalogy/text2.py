def listextends(val, list=[]):
    list.append(val)
    return list


list1 = listextends(10)
list2 = listextends(123,[])
list3 = listextends('a')

print("list1: ", list1)
print("list2: ", list2)
print("list3: ", list3)