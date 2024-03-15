size = int(input())

matrix = []

for i in range(size):
    matrix.append([int(i) for i in input().split()])

Flag = True

for i in range(size):
    for j in range(size):
        if matrix[i][j] != matrix[j][i]:
            Flag = False


print('YES' if Flag else 'NO')