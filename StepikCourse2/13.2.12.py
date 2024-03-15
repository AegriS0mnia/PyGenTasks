from fractions import Fraction as F

from math import gcd

number = int(input())
max_fraction = F(0, 1)
for i in range(number):
    for j in range(number):
        if i + j == number and i < j and gcd(i, j) == 1:
            max_fraction = max(max_fraction, F(i, j))

print(max_fraction)
