rows, columns = int(input()), int(input())
matrix = []

for i in range(rows):
    current_row = [input() for j in range(columns)]
    matrix.append(current_row)

for row in matrix:
    print(*row)

print()

for i in range(columns):
    for j in range(rows):
        print(matrix[j][i], end=' ')
    print()
