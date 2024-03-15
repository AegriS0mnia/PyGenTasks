from math import pi


def get_circle(radius):
    return 2*pi*radius, pi*radius**2


radius = float(input())


print(*get_circle(radius))
