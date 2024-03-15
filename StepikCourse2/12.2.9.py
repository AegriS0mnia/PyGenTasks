from random import randrange

lotteries = set()

while len(lotteries) < 100:
    lottery = str(randrange(1, 10)) + ''.join([str(randrange(10)) for i in range(6)])
    lotteries.add(lottery)

for i in lotteries:
    print(i)


