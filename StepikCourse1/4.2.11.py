number = int(input())

beautiful_number_condition = (1000 <= number <= 9999) and (number % 7 == 0 or number % 17 == 0)

if beautiful_number_condition:
    print('YES')
else:
    print('NO')