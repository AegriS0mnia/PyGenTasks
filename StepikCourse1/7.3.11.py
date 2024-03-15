from math import floor

number = int(input())

sum_of_dividers = number

for i in range(1, number//2 + 1):
    if number % i == 0:
        sum_of_dividers += i

print(sum_of_dividers)
