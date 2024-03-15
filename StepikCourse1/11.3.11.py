number_of_numbers = int(input())
numbers_set = []
sum_ = []

for _ in range(number_of_numbers):
    numbers_set.append(int(input()))


for i in range(1, len(numbers_set)):
    sum_.append(numbers_set[i-1] + numbers_set[i])

print(sum_)