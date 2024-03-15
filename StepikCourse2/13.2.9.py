from fractions import Fraction as F

fraction1, fraction2 = input(), input()

operations = {'+': F(fraction1) + F(fraction2), '-': F(fraction1) - F(fraction2),
              '*': F(fraction1) * F(fraction2), '/': F(fraction1) / F(fraction2)}

for i in operations:
    print(f'{fraction1} {i} {fraction2} = {operations[i]}')
