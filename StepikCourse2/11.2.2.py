line = input().split()
accumulator = []

for i in line:
    accumulator.append(i)
    print(accumulator.count(i), end=' ')
