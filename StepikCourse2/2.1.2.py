a, b = [int(input()) for i in range(2)]

calculations = {'sum_': a + b, 'diff': a - b, 'product': a * b, 'quotient': a / b,
                'true_div': a // b, 'reminder': a % b, 'root_of_degrees': (a**10 + b**10)**0.5}

for calculation in calculations:
    print(calculations[calculation])
