secret_word = input()

symbols = {j: secret_word.count(j) for j in secret_word}

letters = {}
for i in range(int(input())):
    line = input().split(': ')
    letters.setdefault(int(line[1]), line[0])

for key in symbols:
    secret_word = secret_word.replace(key, letters[symbols[key]])

print(secret_word)
