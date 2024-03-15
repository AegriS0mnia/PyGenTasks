size = int(input())

matrix = [[0] * size for i in range(size)]

for i in range(size):
    for j in range(size):
        JCHECK = size - j - 1

        if j == size - i - 1:
            matrix[i][j] = 1
        elif i > JCHECK:
            matrix[i][j] = 2

for row in matrix:
    print(*row)
