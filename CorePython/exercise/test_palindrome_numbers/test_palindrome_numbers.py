number = 15351
r = 0
reverse_number = 0
n = number

while n > 0:
    r = n % 10
    reverse_number = (reverse_number * 10) + r
    n = n // 10

if number == reverse_number:
    print('palindrome number :', reverse_number)
else:
    print('not a palindrome number :', reverse_number)
