month_number = int(input())

if month_number == 2:
    print(28)
elif month_number == 4 or month_number == 6 or month_number == 9 or month_number ==11:
    print(30)
else:
    print(31)
    