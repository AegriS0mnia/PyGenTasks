import copy

size = int(input())
matrix = []

for i in range(size):
    matrix.append([int(i) for i in input().split()])

degree = int(input())

matrix_2 = [[0] * size for i in range(size)]

for k in range(size):
    for m in range(size):
        for i in range(size):
            matrix_2[k][m] += matrix[k][i] * matrix[i][m]
    
for row in matrix_2:
    print(*row)
