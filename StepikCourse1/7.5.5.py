number = int(input())
reversed_number = ''

while number != 0:
    last_digit = number % 10
    reversed_number += str(last_digit)
    number //= 10

print(reversed_number)
