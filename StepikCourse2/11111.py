matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

transponted_matrix =
for row in matrix2:
    for elem in row:

for i in matrix1:
    for j in matrix2:
        res = sum(a*b for a, b in zip(i, j))
        print(res, end=' ')
    print()
