count = 0
maximum = -10 ** 13

for i in range(8):
    number = int(input())
    if number % 4 == 0:
        count += 1
        if number > maximum:
            maximum = number

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
    