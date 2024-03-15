number = int(input())

yes_condition = number % 2 != 0 or (6 <= number <= 20 and number % 2 == 0)

if yes_condition:
    print('YES')
else:
    print('NO')