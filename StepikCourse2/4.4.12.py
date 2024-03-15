rows_columns = int(input())
matrix = []
sum_of_first_quadrant = 0
sum_of_second_quadrant = 0
sum_of_third_quadrant = 0
sum_of_fourth_quadrant = 0

for i in range(rows_columns):
    current_row = [int(j) for j in input().split()]
    matrix.append(current_row)

for i in range(rows_columns):
    for j in range(rows_columns):
        JCHECK = rows_columns - 1 - j
        if i < j and i > JCHECK:
            sum_of_first_quadrant += matrix[i][j]
        elif i < j and i < JCHECK:
            sum_of_second_quadrant += matrix[i][j]
        elif i > j and i < JCHECK:
            sum_of_third_quadrant += matrix[i][j]
        elif i > j and i > JCHECK:
            sum_of_fourth_quadrant += matrix[i][j]

print(f'Верхняя четверть: {sum_of_second_quadrant}')
print(f'Правая четверть: {sum_of_first_quadrant}')
print(f'Нижняя четверть: {sum_of_fourth_quadrant}')
print(f'Левая четверть: {sum_of_third_quadrant}')
