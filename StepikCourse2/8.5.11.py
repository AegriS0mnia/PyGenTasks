number_of_lines = int(input())
unique_symbols_list = []

for i in range(number_of_lines):
    word = input()
    unique_symbols = len(set(word.lower()))
    unique_symbols_list.append(unique_symbols)

print(*unique_symbols_list, sep='\n')

