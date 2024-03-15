number = int(input())

thousands = number // 1000
hundreds = number // 100 % 10
tens = number // 10 % 10
units = number % 10

print('Цифра в позиции тысяч равна', thousands)
print('Цифра в позиции сотен равна', hundreds)
print('Цифра в позиции десятков равна', tens)
print('Цифра в позиции единиц равна', units)