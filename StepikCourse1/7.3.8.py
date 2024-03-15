number_of_terms = int(input())

_sum = 0

for i in range(1, number_of_terms + 1):
    if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
        _sum += i

print(_sum)
