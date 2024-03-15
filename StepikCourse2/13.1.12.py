from decimal import *
num = Decimal(input())

if 0 < abs(num) <= 1:
    num =num.as_tuple()
    print(num[1][-1])
else:
    num = num.as_tuple()
    print(num[1][0] + num[1][-1])
