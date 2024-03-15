from string import digits as ascii_digits
from string import ascii_uppercase
from string import ascii_lowercase
from string import ascii_letters

from random import choice
from random import shuffle


def generate_password(password_length):
    valid_symbols = [i for i in (ascii_letters + ascii_digits) if i not in 'lI1oO0']
    digits = [i for i in ascii_digits if i not in '10']
    capitals = [i for i in ascii_uppercase if i not in 'IO']
    lower = [i for i in ascii_lowercase if i not in 'lo']

    password = ([choice(digits), choice(lower), choice(capitals)] + [choice(valid_symbols) for i in range(password_length -3)])

    shuffle(password)

    return ''.join(password)



def generate_passwords(count, password_length):
    passwords = [generate_password(password_length) for i in range(count)]

    return passwords

count = int(input())
password_length = int(input())

print(*generate_passwords(count, password_length), sep='\n')
