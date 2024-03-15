size = int(input())

matrix = []

for i in range(size):
    matrix.append([int(i) for i in input().split()])

main_diagonal = []
secondary_diagonal = []
for i in range(size):
    for j in range(size):
        if i == j:
             main_diagonal.append(matrix[i][j])
        if j == size - i - 1:
            secondary_diagonal.append(matrix[i][j])

main_diagonal.sort(reverse=True)
secondary_diagonal.sort(reverse=True)

for i in range(size):
    for j in range(size):
        if i == j:
             matrix[i][j], matrix[i][size - i - 1] = secondary_diagonal[i], main_diagonal[i]


for row in matrix:
    print(*row)
