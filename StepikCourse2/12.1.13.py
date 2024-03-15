from string import ascii_letters
from random import choice

print(''.join([choice(ascii_letters) for i in range(int(input()))]))
