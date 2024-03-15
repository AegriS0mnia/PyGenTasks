def get_shipping_cost(quantity):
    cost = 1000 + 120 * (quantity - 1)
    print(cost)


quanity = int(input())

get_shipping_cost(quanity)