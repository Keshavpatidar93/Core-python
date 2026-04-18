number = 153
r = 0
sum = 0
n = number

while n > 0:
    r = n % 10
    sum = sum + (r * r * r)
    n = n // 10                     # do divide sign kyuki isse only integer hi value pick hogi

if sum == number:
    print('armstrong number')
else:
    print('not armstrong number')
