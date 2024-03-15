from math import factorial

number = int(input())
accumulator = 0

for i in range(1, number + 1):
    accumulator += factorial(i)

print(accumulator)