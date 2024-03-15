first_side = int(input())
second_side = int(input())
third_side = int(input())

inequality_of_triangle = (first_side + second_side > third_side and first_side + third_side > second_side
                         and second_side + third_side > first_side)

if inequality_of_triangle:
    print('YES')
else:
    print('NO')
