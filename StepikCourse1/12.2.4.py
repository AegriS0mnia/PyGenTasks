number = input()
digits = [int(i) for i in number.split('-') if i.isdigit()]
digits_str = [str(i) for i in digits]

if len(digits) == 4:
    digits_check = digits[0] == 7 and len(str(digits[1])) == len(str(digits[2])) == 3 and len(str(digits[3])) == 4
    if digits_check:
        if number == '-'.join(digits_str):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
elif len(digits) == 3:
    digits_check = len(str(digits[0])) == len(str(digits[1])) == 3 and len(str(digits[2])) == 4
    if digits_check:
        if number == '-'.join(digits_str):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
