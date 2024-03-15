number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

min_number = min(number_1, number_2, number_3)
max_number = max(number_1, number_2, number_3)
middle_number = (number_1 + number_2 + number_3) - (min_number + max_number)

print(max_number, middle_number, max_number, sep='\n')