def solve(a, b, c):
    root_of_discriminant = (b**2 - 4*a*c)**0.5
    if root_of_discriminant == 0:
        root_1 = root_2 = -b / (2*a)
    else:
        root_1, root_2 = (-b - root_of_discriminant) / (2*a), (-b + root_of_discriminant) / (2*a)

    return sorted([root_1, root_2])


a, b, c = [int(input()) for i in range(3)]

print(*solve(a,b,c))