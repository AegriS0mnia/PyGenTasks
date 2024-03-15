number = int(input())

reversed_binary_number = ''

while number != 0:
    reversed_binary_number += str(number % 2)
    number //= 2

for i in range(-1, -len(reversed_binary_number) - 1, -1):
    print(reversed_binary_number[i], end='')

