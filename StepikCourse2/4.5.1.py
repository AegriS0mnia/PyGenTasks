rows, columns = int(input()), int(input())
matrix = []

for i in range(rows):
    matrix.append([0 for j in range(columns)])

for i in range(rows):
    for j in range(columns):
        matrix[i][j] = str(i * j).ljust(3)

for row in matrix:
    print(*row)
