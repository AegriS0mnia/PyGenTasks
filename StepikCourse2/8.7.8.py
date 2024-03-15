number1, number2 = [set(input()) for i in range(2)]

print('NO' if number1.isdisjoint(number2) else 'YES')

