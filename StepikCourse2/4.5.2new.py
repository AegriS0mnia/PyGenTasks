rows, columns = int(input()), int(input())
maximum = -10**23
indexes_of_max = []
matrix = []

for i in range(rows):
    matrix.append([int(j) for j in input().split()])

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            indexes_of_max = [i, j]

print(*indexes_of_max)