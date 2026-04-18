a = 5
for i in range(2,a):
    for j in range(2,i+1):
        if a%j == 0:
            print("It is not a prime number ")
            exit()
    if i==a-1:
        print("It is a prime number")

