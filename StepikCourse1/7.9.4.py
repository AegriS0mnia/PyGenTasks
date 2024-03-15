number = int(input())

for number in range(1, number + 1):
    counter = 0
    for divider in range(1, number + 1):
        if number % divider == 0:
            counter += 1
    print(str(number) + '+' * counter)




