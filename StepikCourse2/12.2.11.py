from random import shuffle

bingo_list = []


def bingo():
    numbers = [str(i).ljust(3) for i in range(1, 76)][:25]
    shuffle(numbers)

    while numbers:
        bingo_list.append(numbers[:5])
        numbers = numbers[5:]

    bingo_list[2][2] = '0'.ljust(3)


bingo()

for row in bingo_list:
    print(*row)