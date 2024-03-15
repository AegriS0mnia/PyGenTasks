from random import randrange

number_of_flips = int(input())
variants = {0: 'Орел', 1: 'Решка'}

for _ in range(number_of_flips):
    print(variants[randrange(2)])
