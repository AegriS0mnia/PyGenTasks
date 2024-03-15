text = input()
counter_plus = 0
counter_star = 0


for i in text:
    if i == '*':
        counter_star += 1
    if i == '+':
        counter_plus += 1

print('Символ + встречается', counter_plus, 'раз')
print('Символ * встречается', counter_star, 'раз')