number = int(input())

hundreds = number // 100
tens = number // 10 % 10
units = number % 10

sum_of_digits = hundreds + tens + units
product_of_digits = hundreds * tens * units

print('Сумма цифр =', sum_of_digits)
print('Произведение цифр =', product_of_digits)