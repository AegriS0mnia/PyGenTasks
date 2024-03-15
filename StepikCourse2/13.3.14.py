degree, z1, z2 = int(input()), complex(input()), complex(input())

expression = z1**degree + z2**degree + z1.conjugate()**degree + z2.conjugate()**(degree + 1)

print(expression)
