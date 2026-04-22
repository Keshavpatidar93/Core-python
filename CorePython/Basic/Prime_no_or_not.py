a = 7
for i in range(2,a):
    if a%i == 0:
        print("It is not a prime number ")
        exit()
    if i==a-1:
        print("It is a prime number")

