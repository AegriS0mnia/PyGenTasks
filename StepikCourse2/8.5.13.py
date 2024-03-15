text = input().lower()

for i in text:
    if i in '.,;:-?!':
         text = text.replace(i, '')

unique_words_set = set(text.split())

print(len(unique_words_set))