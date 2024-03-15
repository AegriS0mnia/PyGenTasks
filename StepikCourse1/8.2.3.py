count = 0
maximum = -10**9

for i in range(4):
    number = int(input())
    if number % 2 != 0:
        count += 1
        if number > maximum:
            maximum = number

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
