import math
try:
    a = math.exp(1000)
    print("a is:",a)

except OverflowError as Kes:
    print("Error Occur...",Kes)

else:
    print("No exception occur.")

finally:
    print("Finally the code is run completely.")

