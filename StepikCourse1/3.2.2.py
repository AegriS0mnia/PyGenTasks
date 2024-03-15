first_number = int(input())
second_number = int(input())

square_of_sum = first_number**2 + 2*first_number*second_number + second_number**2
sum_of_squares = first_number**2 + second_number**2

print('Квадрат суммы', first_number, 'и', second_number, 'равен', square_of_sum)
print('Сумма квадратов', first_number, 'и', second_number, 'равна', sum_of_squares)