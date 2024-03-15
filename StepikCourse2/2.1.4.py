line = input()

price_in_pennies = len(line) * 60

dollars = price_in_pennies // 100
pennies = price_in_pennies % 100

price = f'{dollars} р. {price_in_pennies} коп.'

print(price)