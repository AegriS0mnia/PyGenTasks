number_of_customers = int(input())

lines = [input() for i in range(number_of_customers)]

customers = set()
items = {}
for line in lines:
    customers.add(line.split()[0])

customers = sorted(list(customers))

random_dict = {}

for customer in customers:
    _items = []
    for line in lines:
        if customer in line:
            line = line.split()
            line = (line[1], int(line[2]))
            _items.append(line)
    items.setdefault(customer, _items)

for customer in customers:
    products = {i[0]: 0 for i in items[customer]}
    for i in items[customer]:
        if i[0] in products:
            products[i[0]] += i[1]
    products_list = []

    for i in products:
        products_list.append([i, products[i]])
    products_list = sorted(products_list)

    random_dict.setdefault(customer, products_list)

for i in random_dict:
    print(f'{i}:')
    for j in random_dict[i]:
        print(*j)


