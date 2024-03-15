from random import randint

print(*[randint(1, 6) for i in range(int(input()))], sep='\n')
