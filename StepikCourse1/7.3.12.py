number_of_terms = int(input())

_sum = 0

for i in range(1, number_of_terms + 1):
    if i % 2 == 0:
        _sum += -i
    else:
        _sum += i

print(_sum)

