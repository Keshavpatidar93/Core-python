a = 10
b = 4
try:
    c = a/b
    print("c = ",c)


except ZeroDivisionError as e:

    # if b==0 par ye chalega
    print('exception:', e)


except ValueError:
    # if we take input from user and the user give any other then integer
     print("Please number hi daalna tha")


except Exception as e:         # it handles all the type of error (parent class of all the classes)
    print('Exception:', e)


else:
    # Jab try me koi error Nahi aaye to ye chalega
    print('else block executed')


finally:
    # Chahe error aaye ya nahi, ye hamesha chalega
    print('finally block executed')