from random import randint

number = []

while len(number) < 7:
    random_number = randint(1, 49)
    if random_number not in number:
        number.append(random_number)

print(*sorted(number))


