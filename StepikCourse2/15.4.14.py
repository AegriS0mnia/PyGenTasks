from math import sqrt
from math import sin

def square(number):
    return number**2


def cube(number):
    return number**3


def root(number):
    return sqrt(number)


def abs_(number):
    return abs(number)


def sinus(number):
    return sin(number)


number = int(input())
operator = input()

operators = {'квадрат': square, 'куб': cube, 'корень': root, 'модуль': abs_, 'синус': sinus}


print(operators[operator](number))
