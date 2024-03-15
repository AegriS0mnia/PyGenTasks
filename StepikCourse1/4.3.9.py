color1 = input()
color2 = input()

if color1 + color2 == 'красныйсиний' or color1 + color2 == 'синийкрасный':
    print('фиолетовый')
elif color1 + color2 == 'красныйжелтый' or color1 + color2 == 'желтыйкрасный':
    print('оранжевый')
elif color1 + color2 == 'синийжелтый' or color1 + color2 == 'желтыйсиний':
    print('зеленый')
elif color1 == color2:
    print(color1)
else:
    print('ошибка цвета')