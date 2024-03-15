def is_valid_triangle(first_side, second_side, third_side):
    inequality_of_triangle = (first_side + second_side > third_side and first_side + third_side > second_side
                              and second_side + third_side > first_side)

    return inequality_of_triangle


first_side = int(input())
second_side = int(input())
third_side = int(input())

print(is_valid_triangle(first_side, second_side, third_side))