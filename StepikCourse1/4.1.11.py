number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
number_4 = int(input())

comparison_of_1_2 = 0
comparison_of_3_4 = 0
comparison_of_last_pair = 0

if number_1 < number_2:
    comparison_of_1_2 = number_1
else:
    comparison_of_1_2 = number_2
if number_3 < number_4:
    comparison_of_3_4 = number_3
else:
    comparison_of_3_4 = number_4
if comparison_of_1_2 < comparison_of_3_4:
    comparison_of_last_pair = comparison_of_1_2
else:
    comparison_of_last_pair = comparison_of_3_4

print(comparison_of_last_pair)
