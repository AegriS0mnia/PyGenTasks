import copy

rows, columns = [int(i) for i in input().split()]

vector = [i for i in range(1, rows * columns + 1)]
matrix = [[0] * columns for j in range(rows)]
ordered_indexes = []
matrix_copy = copy.deepcopy(matrix)

counter = 0
d_x, d_y = 0, 1
while counter <= rows * columns:
    for i in range(rows):
        matrix[d_x][i] = counter
        counter += 1
    for i in range(rows):
        matrix[i][rows - 1] = counter
        counter += 1
    for i in range(rows):
        matrix[rows- 1][rows - 1 - i ] = counter
        counter += 1

for row in matrix:
    print(*row)

print(ordered_indexes)