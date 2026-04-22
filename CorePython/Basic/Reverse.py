number = 123454321
n=number
r=0
revese = 0
while n>0:
    r = n%10
    revese = (revese*10)+r
    n=n//10
if revese == number:
    print("the number ",number," is a reverse number")
else:
    print("the number ",number," is not a reverse number")