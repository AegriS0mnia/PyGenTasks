def print_products(*args):
    counter = 0
    products = [i for i in args if type(i) == str and i != '']

    if len(products) == 0:
        print('Нет продуктов')
    else:
        for i in range(1, len(products) + 1):
            print(f'{i}) {products[i - 1]}')
