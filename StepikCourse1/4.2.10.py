number = int(input())

condition_of_inclusion = -30 < number <= -2 or 7 < number <= 25

if condition_of_inclusion:
    print('Принадлежит')
else:
    print('Не принадлежит')