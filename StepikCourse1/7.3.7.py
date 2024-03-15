from math import log

number_of_terms = int(input())

_sum = 0

for i in range(1, number_of_terms + 1):
    _sum += 1 / i

asymptotic_approximation = _sum - log(number_of_terms)

print(asymptotic_approximation)
