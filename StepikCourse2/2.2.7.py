players = ['Тимур', 'Руслан']

choice1, choice2 = input(), input()

rules = {'каменьножницы': 0, 'ножницыкамень': 1,
         'бумагакамень': 0, 'каменьбумага': 1,
         'ножницыбумага':0 , 'бумаганожницы': 1}

if choice1 + choice2 in rules:
    print(players[rules[choice1 + choice2]])
else:
    print('ничья')

