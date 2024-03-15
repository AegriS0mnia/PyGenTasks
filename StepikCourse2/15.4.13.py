from operator import itemgetter

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


def sort_by_name(athletes):
    return sorted(athletes, key=itemgetter(0))


def sort_by_age(athletes):
    return sorted(athletes, key=itemgetter(1))


def sort_by_height(athletes):
    return sorted(athletes, key=itemgetter(2))


def sort_by_weight(athletes):
    return sorted(athletes, key=itemgetter(3))



command = int(input())
commands = {1: sort_by_name, 2: sort_by_age, 3: sort_by_height, 4: sort_by_weight}

for i in commands[command](athletes):
    print(*i)

