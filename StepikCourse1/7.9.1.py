number = int(input())

accumulator = 1

for i in range(1, number + 1):
    for j in range(i):
        print(accumulator, end=' ')
        accumulator += 1
    print()
