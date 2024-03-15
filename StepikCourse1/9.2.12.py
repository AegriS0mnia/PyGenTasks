string = input()

string_length = len(string)
string_x3 = string * 3
first_symbol = string[0]
first_three_symbols = string[:3]
last_three_symbols = string[-3:]
reversed_string = string[::-1]
cutted_string = string[1:len(string) - 1]

print(string_length, string_x3, first_symbol, first_three_symbols, sep='\n')
print(last_three_symbols, reversed_string, cutted_string, sep='\n')
