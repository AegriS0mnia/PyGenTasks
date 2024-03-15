from string import ascii_uppercase as as_up
from random import choice
from random import randrange

def generate_index():
    return f'{choice(as_up)}{choice(as_up)}{randrange(100)}_{randrange(100)}{choice(as_up)}{choice(as_up)}'
