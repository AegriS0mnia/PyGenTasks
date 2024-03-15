rows, columns = [int(i) for i in input().split()]

matrix_1 = []
matrix_2 = []
matrix_3 = [[0] * columns for i in range(rows)]

for i in range(rows):
    matrix_1.append(list(map(int, input().split())))

emplty_line = input()

for i in range(rows):
    matrix_2.append(list(map(int, input().split())))

for i in range(rows):
    for j in range(columns):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]

for row in matrix_3:
    print(*row)
