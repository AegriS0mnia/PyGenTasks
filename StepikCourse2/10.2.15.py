symbols = {'.': '1',
           ',': '11',
           '?':'111',
           '!': '1111',
           ':': '11111',
           'a':'2',
           'b': '222',
           'c': '22222',
           'd': '3',
           'e': '333',
           'f': '33333',
           'g': '4',
           'h': '444',
           'i': '44444',
           'j': '5',
           'k': '555',
           'l': '55555',
           'm': '6',
           'n': '666',
           'o': '66666',
           'p': '7',
           'q': '777',
           'r': '77777',
           's': '7777777',
           't': '8',
           'u': '888',
           'v': '88888',
           'w': '9',
           'x': '999',
           'y': '99999',
           'z': '9999999',
           ' ': '0'}

message = input()

for letter in message:
    if letter.lower() in symbols:
        if letter.isalpha() and letter.isupper():
            letter = letter.lower()
            print(symbols[letter] + symbols[letter][0], end='')
        else:
            print(symbols[letter], end='')
    else:
        continue
