from string import punctuation
from operator import itemgetter

line = ''.join([i for i in input().lower() if i not in punctuation])

unique_words = set(word for word in line.split())

words_counter = [line.split().count(word) for word in unique_words]

dictionary = list(zip(unique_words, words_counter))

sorted_dict = sorted(dictionary, key=lambda x: (x[1], x[0]))

print(sorted_dict[0][0])
