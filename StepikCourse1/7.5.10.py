number = int(input())

flag = False

while number >= 10:
    if number % 10 > number // 10 % 10:
        flag = True
    number //= 10

if flag:
    print('NO')
else:
    print('YES')