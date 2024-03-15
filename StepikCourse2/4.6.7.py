rows, columns = [int(i) for i in input().split()]

vector = [i for i in range(1, columns + 1)]
matrix = [[0] * columns for j in range(rows)]

for i in range(rows):
    for j in range(len(vector)):
        matrix[i][j] = vector[j]

    vector = vector[1:] + [vector[0]]

for row in matrix:
    print(*row)