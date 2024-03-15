with open('forbidden_words.txt', 'r', encoding='utf-8') as forbidden_words, open('data.txt', 'r+', encoding='utf-8') as data:
    forbidden_words = [word for word in forbidden_words.readline().split()]
    data = data.readlines()
    filtered_data = []
    new_data = []
    for line in data:
        line = line.lower()
        for word in forbidden_words:
            if word in line:
                line = line.replace(word, '*' * len(word))
        filtered_data.append(line)

    for line_index in range(len(filtered_data)):
        for letter_index in range(len(filtered_data[line_index])):
            if filtered_data[line_index][letter_index] == '*':
                print('*', end='')
            else:
                print(data[line_index][letter_index], end='')