import string

number = input()
chunks = [i for i in number.split('.')]

is_non_negative_num = lambda number: len(number) <= 2

print(chunks)