try:
    a = int(input("Enter a number :"))
    if(a > 10):
        raise Exception("Invalid..... Number greater than 10")          # raise keyword is use that throws the exception to the particular exception class

except Exception as kes:
    print("Exception.",kes)
