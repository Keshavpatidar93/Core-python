list1 = []
list2 = []
n = int(input("Enter number of elements in a list 1 "))
print("Enter the number of elements in list 1 :")
for i in range(0,n):
    list1.append(int(input("Enter element")))
print("Enter the number of elements in list 2 :")
for i in range(0,n-1):
    list2.append(int(input("Enter element")))

missing = 0
for a in list1:
    missing = missing ^a   # xor is the most optimun method to find unique element
for b in list2:
    missing = missing ^b
print("The missing element in list 2 is :",missing)