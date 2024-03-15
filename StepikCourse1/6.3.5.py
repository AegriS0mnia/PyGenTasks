from math import tan
from math import sin
from math import cos
from math import radians

angle = float(input())

angle_in_rads = radians(angle)

trigonometric_function = sin(angle_in_rads) + cos(angle_in_rads) + tan(angle_in_rads)**2

print(trigonometric_function)