numbers_file = open('numbers.txt', encoding='utf-8')

numbers_list = (int(numbers_file.readline()) for i in range(2))

sum_of_numbers = sum(numbers_list)

print(sum_of_numbers)

numbers_file.close()
