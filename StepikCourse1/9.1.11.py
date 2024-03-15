text = input()
is_digit_here = False

for i in text:
    if i in '0123456789':
        is_digit_here = True
        break

if is_digit_here:
    print('Цифра')
else:
    print('Цифр нет')
