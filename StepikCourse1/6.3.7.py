a, b, c = float(input()), float(input()), float(input())

discriminant = (b**2 - (4*a*c))
root_of_discriminant = discriminant**0.5

if discriminant == 0:
    root = -b / (2 * a)
    print(root)
elif discriminant < 0:
    print('Нет корней')
else:
    root_1 = (-b - root_of_discriminant)/(2*a)
    root_2 = (-b + root_of_discriminant)/(2*a)
    print(min(root_1, root_2), max(root_1, root_2), sep='\n')
