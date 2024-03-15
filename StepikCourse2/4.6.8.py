rows, columns = [int(i) for i in input().split()]

vector = [i for i in range(1, rows * columns + 1)]
matrix = [[0] * columns for j in range(rows)]

for i in range(rows):
    if i % 2 == 0:
        matrix[i] = vector[:columns]
    else:
        matrix[i] = vector[:columns][::-1]

    vector = vector[columns:]

for row in matrix:
    print(*row)