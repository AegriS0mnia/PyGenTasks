string = input()

third_symbol = string[2]
penultimate_symbol = string[-2]
first_five_symbols = string[:5]
string_without_last2 = string[:len(string) - 2]
even_symbols = string[::2]
odd_symbols = string[1::2]
reversed_string = string[::-1]
odd_symbols_from_end = string[::-2]

print(third_symbol, penultimate_symbol, first_five_symbols, string_without_last2, sep='\n')
print(even_symbols, odd_symbols, reversed_string, odd_symbols_from_end, sep='\n')
