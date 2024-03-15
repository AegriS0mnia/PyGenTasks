number = int(input())

for i in range(1, number + 1):
    if i == 1 or i == number:
        print('*' * 19)
    else:
        print('*' + ' ' * 17 + '*')
