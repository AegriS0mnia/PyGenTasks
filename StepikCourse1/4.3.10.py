number = int(input())
if number == 0:
    print('зеленый')
elif 1 <= number <= 10:
    if number % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= number <= 18:
    if number % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= number <= 28:
    if number % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= number <= 36:
    if number % 2 == 0:
        print('красный')
    else:
        print('черный')
else:
    print('ошибка ввода')