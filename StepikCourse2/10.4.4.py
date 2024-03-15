words_quantity = int(input())

dictionary = {}

for i in range(words_quantity):
    pair = input().split()
    dictionary.setdefault(pair[0], pair[1])
    dictionary.setdefault(pair[1], pair[0])

query = input()

print(dictionary[query])