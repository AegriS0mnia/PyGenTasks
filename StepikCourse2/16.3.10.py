number_of_words = int(input())

words = [input() for i in range(number_of_words)]
gematries = []

for word in words:
    word_gematry = sum([ord(i.upper()) - ord('A') for i in word])
    gematries.append(word_gematry)
words_and_gematries = zip(gematries, words)

sorted_words = sorted(words_and_gematries)

for word in sorted_words:
    print(word[1])
