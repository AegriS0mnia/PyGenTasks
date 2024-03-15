def convert_to_python_case(camel_case):
    capital_indexes = []
    words = []
    for c in range(len(camel_case)):
        if camel_case[c] == camel_case[c].upper() and not(camel_case[c].isdigit()):
            capital_indexes.append(c)

    for i in range(1, len(capital_indexes)):
        word = camel_case[capital_indexes[i - 1]: capital_indexes[i]]
        words.append(word.lower())
    words.append(camel_case[max(capital_indexes):].lower())
    python_case = '_'.join(words)

    return python_case

camel_case = input()

print(convert_to_python_case(camel_case))
