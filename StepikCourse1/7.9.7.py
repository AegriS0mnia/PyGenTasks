from math import ceil

a, b = int(input()), int(input())

for number in range(a, b + 1):
    counter = 0

    for divider in range(2, ceil(number**0.5) + 1):
        if number % divider == 0:
            counter += 1
    if (counter == 0 and number >= 2) or number == 2:
        print(number)
