first_quadrant = 0
second_quadrant = 0
third_quadrant = 0
fourth_quadrant = 0

matrix = []

number_of_coordinates = int(input())

for i in range(number_of_coordinates):
    matrix.append([int(j) for j in input().split()])

for i in range(len(matrix)):
    if matrix[i][0] == 0 or matrix[i][1] == 0:
        continue
    if matrix[i][0] < 0:
        if matrix[i][1] > 0:
            second_quadrant += 1
        else:
            third_quadrant += 1
    else:
        if matrix[i][1] > 0:
            first_quadrant += 1
        else:
            fourth_quadrant += 1

print(f'Первая четверть: {first_quadrant}')
print(f'Вторая четверть: {second_quadrant}')
print(f'Третья четверть: {third_quadrant}')
print(f'Четвертая четверть: {fourth_quadrant}')
