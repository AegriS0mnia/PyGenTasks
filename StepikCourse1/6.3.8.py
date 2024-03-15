from math import tan
from math import pi

number_of_sides = float(input())
length_of_side = float(input())

area_of_polygon = (number_of_sides*length_of_side**2) / (4*tan(pi/number_of_sides))

print(area_of_polygon)