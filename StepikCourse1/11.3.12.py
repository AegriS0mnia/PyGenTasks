number_of_numbers = int(input())
number_set = []

for _ in range(number_of_numbers):
    number = int(input())
    number_set.append(number)

del number_set[1::2]

print(number_set)