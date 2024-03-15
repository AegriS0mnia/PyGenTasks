from operator import itemgetter

numbers = [int(i) for i in input().split()]
sums_of_digits = [sum(map(int, list(str(i)))) for i in numbers]
sums_and_its_sums = sorted(zip(sums_of_digits, numbers), key=itemgetter(0))

for number in sums_and_its_sums:
    print(number[1], end=' ')
