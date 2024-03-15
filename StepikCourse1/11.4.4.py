number_of_numbers = int(input())
numbers_set = []
cleared_set = []

for i in range(number_of_numbers):
    numbers_set.append(int(input()))

max_number = max(numbers_set)
min_number = min(numbers_set)

for num in numbers_set:
    if num != max_number and num != min_number:
        cleared_set.append(num)


print(*cleared_set, sep='\n')
