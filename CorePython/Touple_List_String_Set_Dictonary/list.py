list = [1,3.09,"Hello",True,"Keshav",4,8]
print(list)

for i in list:  # for loop in the list
    print(i)

print(list*2) #it print the list for two times

list.append(9) #it insert the element into the last of the list
print(list)

list.insert(1,2) #it insert the element at the particular index
print(list)

list.pop()   # it deletes the last element of the list
print(list)

list.pop(0)   # it deletes the particular index element of the list
print(list)

list.remove(2)  # it removes the particular value
print(list)

list1 = [10,51,22,94,37,89,64,45]
list1.sort()    # it sort the element in the real list means not make its duplicate
print(list1)

copyyyyy = list.copy()   # it makes the copy of the original list
print(copyyyyy)

copyyyyy.clear()
print(copyyyyy)  # it clear the element in the real list means not make its duplicate

list.extend(["World",False,77])  # it extends(adds new elements )the list
print(list)

reverse = list.reverse()  # it reverse all the list elements
print(list)

t = tuple(list)  # it converts the list into tuple
print(t)
print(type(list))