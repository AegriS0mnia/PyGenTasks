number = int(input())

sum_of_digits = 0
number_of_digits = 0
product_of_digits = 1
average = 0
first_digit = 0
sum_of_first_and_last_digit = 0

while number != 0:
    last_digit = number % 10
    number_of_digits += 1
    sum_of_digits += last_digit
    product_of_digits *= last_digit
    if number_of_digits == 1:
        sum_of_first_and_last_digit += last_digit
    if number < 10:
        first_digit = last_digit
        sum_of_first_and_last_digit += last_digit
    number //= 10

average = sum_of_digits / number_of_digits

print(sum_of_digits, number_of_digits, product_of_digits, average, first_digit, sum_of_first_and_last_digit, sep='\n')

