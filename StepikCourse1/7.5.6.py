number = int(input())

min_digit = 9
max_digit = -1

while number != 0:
    last_digit = number % 10
    min_digit = min(min_digit, last_digit)
    max_digit = max(max_digit, last_digit)
    number //= 10

print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)
