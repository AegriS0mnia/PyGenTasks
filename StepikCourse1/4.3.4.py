side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

equilateral_triangle = side_1 == side_2 == side_3
isosceles_triangle = side_1 == side_2 or side_2 == side_3 or side_1 == side_3

if equilateral_triangle:
    print('Равносторонний')
elif isosceles_triangle:
    print('Равнобедренный')
else:
    print('Разносторонний')