complex1, complex2 = complex(input()), complex(input())

operations = {'+': complex1 + complex2, '-': complex1 - complex2,
              '*': complex1 * complex2}

for i in operations:
    print(f'{complex1} {i} {complex2} = {operations[i]}')
