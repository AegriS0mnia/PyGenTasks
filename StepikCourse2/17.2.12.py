from random import randrange

text = open('lines.txt', encoding='utf-8')

content = text.readlines()

string_number = randrange(1, len(content))

print(content[string_number])

text.close()
