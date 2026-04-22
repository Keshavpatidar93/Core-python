list = [12,53,84,96,56,74,87,32,65]
largest = 0
second_largest = 0
for i in list:
    if i>largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("Largest  value is : ",largest)
print("Second largest value is : ",second_largest)
