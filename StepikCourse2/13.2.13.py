from fractions import Fraction as F

from math import gcd


number = int(input())
fractions = []

for i in range(1, number + 1):
    for j in range(1, number + 1):
        if gcd(i, j) == 1 and i < j:
            fractions.append(F(i, j))


print(*sorted(fractions), sep='\n')