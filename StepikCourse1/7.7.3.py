count = 0
product = 1

for _ in range(10):
    number = int(input())
    if number >= 0:
        product *= number
        count += 1

if count > 0:
    print(count)
    print(product)
else:
    print('NO')
