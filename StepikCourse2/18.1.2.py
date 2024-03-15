with open('ledger.txt', 'r', encoding='utf-8') as ledger:
    print('$' + str(sum([int(price[1:]) for price in ledger.readlines()])))
