prices_file = open('prices.txt', encoding='utf-8')

price_lines = [list(map(int, line.split()[1:])) for line in prices_file.readlines()]

total_price = sum(i[0] * i[1] for i in price_lines)

print(total_price)

prices_file.close()
