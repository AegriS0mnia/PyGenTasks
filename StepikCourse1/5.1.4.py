number = int(input())

if number > 10:
    print('ошибка')
if number != 4 and number != 9 and number != 10:
    print('V'*(number // 5) + 'I'*abs(number % 5))
elif number == 4:
    print('IV')
elif number == 9:
    print('IX')
else:
    print('X')
