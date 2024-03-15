text = input()
counter = 0
dictionary = 'abcdefghijklmnopqrstuvwxyz'

for c in text:
    if c in dictionary:
        counter += 1

print(counter)