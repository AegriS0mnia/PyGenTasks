number = int(input())
max_digit = -1

while number > 0:
    last_digit = number % 10
    if last_digit % 3 == 0:
        max_digit = max(last_digit, max_digit)
    number //= 10

if max_digit == -1:
    print('NO')
else:
    print(max_digit)
