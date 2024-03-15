number = int(input())

units = number % 10
counter_3 = 0
counter_last = 0
counter_even = 0
sum_more_than_5 = 0
product_of_more_than_7 = 1
counter_5_and_0 = 0

while number != 0:
    last_digit = number % 10
    if last_digit == 3:
        counter_3 += 1
    if last_digit == units:
        counter_last += 1
    if last_digit % 2 == 0:
        counter_even += 1
    if last_digit > 5:
        sum_more_than_5 += last_digit
    if last_digit > 7:
        product_of_more_than_7 *= last_digit
    if last_digit == 5 or last_digit == 0:
        counter_5_and_0 += 1
    number //= 10
print(counter_3, counter_last, counter_even, sum_more_than_5, product_of_more_than_7, counter_5_and_0, sep='\n')