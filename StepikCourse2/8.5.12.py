number_of_lines = int(input())
unique_symbols_set = set()

for i in range(number_of_lines):
    word = list(input().lower())
    for j in word:
        unique_symbols_set.add(j)

print(len(unique_symbols_set))

