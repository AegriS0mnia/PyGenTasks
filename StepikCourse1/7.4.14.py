price = int(input())

amount_of_coins = 0

while price >= 25:
    amount_of_coins += price // 25
    price = price % 25

while price >= 10:
    amount_of_coins += price // 10
    price = price % 10

while price >= 5:
    amount_of_coins += price // 5
    price = price % 5

print(amount_of_coins + price)
