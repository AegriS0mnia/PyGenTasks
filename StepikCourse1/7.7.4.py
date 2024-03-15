max_negative = -10 ** 7  # 1
_sum = 0

for _ in range(10):  # 2
    number = int(input())
    if number < 0:
        _sum += number
        max_negative = max(number, max_negative)

if _sum != 0:
    print(_sum)
    print(max_negative)
else:
    print('NO')

