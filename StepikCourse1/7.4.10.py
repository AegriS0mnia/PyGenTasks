word = input()

word_counter = 0
while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    word_counter += 1
    word = input()

print(word_counter)
