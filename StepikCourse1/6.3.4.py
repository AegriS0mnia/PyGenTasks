from math import  sqrt

number1, number2 = float(input()), float(input())

average = (number1 + number2) / 2
geometric_mean = sqrt((number1 * number2))
harmonic_mean = (2*number1*number2) / (number1 + number2)
root_mean_square = sqrt((number1**2 + number2**2) / 2)

print(average, geometric_mean, harmonic_mean, root_mean_square, sep='\n')