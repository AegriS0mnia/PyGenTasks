size = int(input())

matrix = []

for i in range(size):
    matrix.append(list(map(int, input().split())))


sums_of_rows = []
sums_of_columns = []
sum_of_main_diagonal = 0
sum_of_secondary_diagonal = 0
nums = []
_range = [i for i in range(1, size**2 + 1)]

for i in range(size):
    sum_of_row = 0
    sum_of_column = 0
    for j in range(size):
        nums.append(matrix[i][j])
        sum_of_row += matrix[i][j]
        sum_of_column += matrix[j][i]

        if i == j:
            sum_of_main_diagonal += matrix[i][j]
        if j == size - i - 1:
            sum_of_secondary_diagonal += matrix[i][j]
    sums_of_rows.append(sum_of_row)
    sums_of_columns.append(sum_of_column)

nums.sort()

is_all_sums_valid = (sums_of_columns == sums_of_rows) and sums_of_columns[0] == sums_of_columns[0] == sum_of_secondary_diagonal == sum_of_main_diagonal
is_all_nums_different = nums == _range


print('YES' if (is_all_sums_valid and is_all_nums_different) else 'NO')