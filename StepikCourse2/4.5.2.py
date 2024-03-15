rows, columns = [int(i) for i in input().split()]

matrix = []
numbers = [num for num in range(1, rows * columns + 1)]

for i in range(rows):
    matrix.append(numbers[:columns])
    numbers = numbers[columns:]

for row in matrix:
    for j in row:
        print(str(j).ljust(3), end=' ')
    print()