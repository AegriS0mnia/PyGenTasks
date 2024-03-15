year = int(input())

leap_year_condition = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

if leap_year_condition:
    print('YES')
else:
    print('NO')