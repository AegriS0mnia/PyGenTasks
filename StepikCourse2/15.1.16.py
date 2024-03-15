def matrix(rows=1, column=None, filler=0):
    matrix_ = []
    if column is None:
        for i in range(rows):
            current_row = [filler] * rows
            matrix_.append(current_row)
    else:
        for i in range(rows):
            current_row = [filler] * column
            matrix_.append(current_row)
    return matrix_


rows = int(input())
column = int(input())
filler = int(input())
print(matrix(rows, column, filler))
