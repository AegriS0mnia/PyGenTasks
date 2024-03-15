rows, columns = int(input()), int(input())

matrix = []

for i in range(rows):
    matrix.append([int(i) for i in input().split()])


column1, column2 = map(int, input().split())

for i in range(rows):
    matrix[i][column1], matrix[i][column2] = matrix[i][column2], matrix[i][column1]

for i in matrix:
    print(*i)