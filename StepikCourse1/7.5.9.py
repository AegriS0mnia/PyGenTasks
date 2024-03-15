number = input()

if number == str((int(number) % 10)) * len(number):
    print('YES')
else:
    print('NO')
