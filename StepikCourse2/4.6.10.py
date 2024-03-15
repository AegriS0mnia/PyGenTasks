import copy

rows, columns = [int(i) for i in input().split()]

vector = [i for i in range(1, rows * columns + 1)]
matrix = [[0] * columns for j in range(rows)]
ordered_indexes = []
matrix_copy = copy.deepcopy(matrix)
for i in range(rows):
    for j in range(columns):
        matrix[i][j] = f'{i}{j}'
for i in range(rows):
    for j in range(columns):
        if i <= j:
            matrix[i][j] = '▶'.ljust(5)
            if i > rows - 1 - j:
                matrix[i][j] = '↓'.ljust(5)
        else:
                matrix[i][j] = '◀'.ljust(5)
                if i < rows - 1 - j:
                    matrix[i][j] = '⬆'.ljust(5)

    vector = vector[1:] + [vector[0]]

for row in matrix:
    print(*row)

print(ordered_indexes)