import math
try:
    a = math.exp(1000)             # here e ki power 1000 is out of the range to store thats why it give overflow error
    print("a is:",a)

except OverflowError as Kes:
    print("Error Occur...",Kes)

else:
    print("No exception occur.")

finally:
    print("Finally the code is run completely.")

