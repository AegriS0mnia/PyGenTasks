from random import randint

with open('random.txt', 'a', encoding='utf-8') as output:
    output.writelines([f'{str(randint(111, 777))}\n' for i in range(25)])
