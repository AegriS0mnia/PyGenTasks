number = int(input())


def pascal_triangle(number):
    layers = []

    for i in range(1, number + 1):
        layers.append([0] * i)

    for layer in layers:
        layer[0], layer[-1] = 1, 1

    for i in range(2, len(layers)):

        for j in range(1, i):
            layers[i][j] = sum(layers[i - 1][j - 1: j + 1])

    return layers

for i in pascal_triangle(number):
    print(*i)
