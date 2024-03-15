word1, word2, word3 = (set(list(i)) for i in input().split())

print('YES' if word1 == word2 == word3 else 'NO')

