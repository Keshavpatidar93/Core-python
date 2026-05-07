try:
    a = 81
    b = int(input("Enter a number : "))
    c = a / b
    print("the value of the c is :",c)

except ZeroDivisionError as message:
    print("Exception --->",message)

except ValueError as kes:       # if in any particular datatype other type of value is come
    print("Exception --->",kes)

except Exception as e:
    print("Exception --->",e)

else :
    print("No exception occurs")

finally:
    print("All the task is executed")