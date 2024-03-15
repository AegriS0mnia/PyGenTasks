rows, columns = [int(i) for i in input().split()]
zero_matrix = [[0] * columns for i in range(rows)]

for i in range(rows):
    for j in range(columns):
        if i % 2:
            if j % 2:
                zero_matrix[i][j] = '.'
            else:
                zero_matrix[i][j] = '*'
        else:
            if j % 2:
                zero_matrix[i][j] = '*'
            else:
                zero_matrix[i][j] = '.'

for i in zero_matrix:
    print(*i)