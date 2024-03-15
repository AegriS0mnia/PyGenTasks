rows, columns = [int(i) for i in input().split()]

vector = [i for i in range(1, rows * columns + 1)]
matrix = [[0] * columns for j in range(rows)]
ordered_indexes = []

for m in range(rows + columns - 1):
    for i in range(m + 1):
        for j in range(m + 1):
            if i + j == m and i < rows and j < columns:
                ordered_indexes.append([i, m - i])

for i in ordered_indexes:
    matrix[i[0]][i[1]] = vector[0]
    vector = vector[1:]

for row in matrix:
     print(*row)