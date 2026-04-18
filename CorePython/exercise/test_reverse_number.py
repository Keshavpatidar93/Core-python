number = 12345
r = 0
reverse_number = 0
n = number

while n > 0:
    r = n % 10
    reverse_number = (reverse_number * 10) + r
    n = n // 10

print('reverse number :', reverse_number)
