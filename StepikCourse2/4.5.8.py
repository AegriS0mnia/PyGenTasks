matrix = []

for i in range(8):
    matrix.append(['.'.ljust(3)] * 8)

position = input()
Y1, X1 = 8 - int(position[1]), ord(position[0]) - ord('a')

matrix[Y1][X1] = 'N'.ljust(3)


for i in range(8):
    for j in range(8):
        if (abs(Y1 - i) == 2 and abs(X1 - j) == 1) or (abs(Y1 - i) == 1 and abs(X1 - j) == 2):
            matrix[i][j] = '*'.ljust(3)

for i in matrix:
    print(''.join(i))
