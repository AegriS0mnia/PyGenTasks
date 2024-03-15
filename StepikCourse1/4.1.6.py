number = int(input())

thousands = number // 1000
hundreds = number // 100 % 10
tens = number // 10 % 10
units = number % 10

condition = thousands + units == hundreds - tens

if condition:
    print("ДА")
else:
    print("НЕТ")