from math import sqrt

X1, Y1 = float(input()), float(input())
X2, Y2 = float(input()), float(input())

euclidian_distance = sqrt((X1 - X2)**2 + (Y1 - Y2)**2)

print(euclidian_distance)