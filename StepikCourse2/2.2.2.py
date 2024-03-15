counter = 0
numbers = [int(i) for i in input().split()]

for i in range(1, len(numbers)):
    if numbers[i-1] < numbers[i]:
        counter += 1

print(counter)
