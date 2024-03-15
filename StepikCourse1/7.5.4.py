number = int(input())

while number != 0:
    last_digit = number % 10
    print(last_digit)
    number //= 10
