size = int(input())

matrix = []
matrix_2 = [[0] * size for j in range(size)]

for i in range(size):
    current_row = [int(j) for j in input().split()]
    matrix.append(current_row)

for i in range(size):
    for j in range(size):
        matrix_2[i][j] = matrix[size - j - 1][i]


for i in matrix_2:
    print(*i)

