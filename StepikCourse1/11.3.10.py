from math import ceil

number = int(input())

dividers_list = []

for i in range(1, ceil(number**0.5) + 1):
    if number % i == 0:
        dividers_list.append(i)
        if number // i == i:
            continue
        dividers_list.append(number // i)
dividers_list.sort()

print(dividers_list)