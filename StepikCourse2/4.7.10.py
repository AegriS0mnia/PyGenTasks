rows_1, columns_1 = [int(i) for i in input().split()]

matrix_1 = []
matrix_2 = []

for i in range(rows_1):
    matrix_1.append([int(i) for i in input().split()])

empty_line = input()

rows_2, columns_2 = [int(i) for i in input().split()]

for i in range(rows_2):
    matrix_2.append([int(i) for i in input().split()])

matrix_3 = [[0] * rows_1 for i in range(columns_2)]


for k in range(rows_1):
    for m in range(columns_2):
        for i in range(columns_1):
            matrix_3[k][m] += matrix_1[k][i] * matrix_2[i][m]

for row in matrix_3:
    print(*row)
