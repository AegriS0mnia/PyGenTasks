number = int(input())

hundreds = number // 100
tens = number // 10 % 10
units = number % 10

min_digit = min(hundreds, tens, units)
max_digit = max(hundreds, tens, units)
middle_digit = (hundreds + tens + units) - (min_digit + max_digit)

if max_digit - min_digit == middle_digit:
    print('Число интересное')
else:
    print('Число неинтересное')
