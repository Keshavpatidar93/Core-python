list = []
n = int(input("Enter the number of elements in a list "))
for i in range(0,n):
    list.append((int(input("Enter a number "))))
key = int(input("Enter any number in the above list"))

def display(list):
    for i in range(0, n + 1):
        if i == key:
            return i-1
        if(i == n):
            return -1


print(display(list))
