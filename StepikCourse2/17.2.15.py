numbers_file = open('numbers.txt', encoding='utf-8')

numbers_sum = sum(map(int, numbers_file.read().split()))

print(numbers_sum)

numbers_file.close()
