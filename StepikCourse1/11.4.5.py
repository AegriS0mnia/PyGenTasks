number_of_strings = int(input())
words_set = []

for _ in range(number_of_strings):
    word = input()
    if word not in words_set:
        words_set.append(word)

print(*words_set, sep='\n')
