number_string = input()
sum_of_digits = 0

for i in range(len(number_string)):
    sum_of_digits += int(number_string[i])

print(sum_of_digits)
