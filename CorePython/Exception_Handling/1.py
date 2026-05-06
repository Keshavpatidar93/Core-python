a = 10
b = 0
try:           # checks if any error are occur or not
    c = a/b
    print("a/b is :",c)

except ZeroDivisionError as Kes:        # except block runs when error occur
    print("Error Occur...",Kes)

else:                                       # else block runs when no error occurs
    print("No exception occur.")

finally:                                           # The finally block always runs in all the cases
    print("Finally the code is run completely.")

