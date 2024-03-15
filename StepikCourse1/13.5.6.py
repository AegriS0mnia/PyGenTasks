def is_one_away(word1, word2):
    counter = 0
    answer = False

    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                counter += 1
    if counter == 1:
        answer = True

    return answer


word1, word2 = input(), input()

print(is_one_away(word1, word2))
