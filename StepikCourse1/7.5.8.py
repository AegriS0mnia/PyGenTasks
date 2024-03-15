number = int(input())

while number != 0:
    last_digit = number % 10
    if 10 <= number <= 99:
        second_digit = last_digit
    number //= 10

print(second_digit)