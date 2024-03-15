line = input().split()
numbers_list = []

for i in line:
    numbers_list.append(int(i))
max_index = numbers_list.index(max(numbers_list))
min_index = numbers_list.index(min(numbers_list))

numbers_list[min_index], numbers_list[max_index] = numbers_list[max_index], numbers_list[min_index]

print(*numbers_list)