print("Initially.....")
a = 10
b = 0
print("Middle......")

try:
    c = a / b
    print(c)

except ZeroDivisionError as e:
    print("Can't divide by 0....",e)

except Exception as ke:
    print(ke)

print("After......")

#here our code is completely running as division by 0 gives the error and it is handled by try except blocks that's why the remaining code is running