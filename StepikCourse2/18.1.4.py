with open('words.txt', 'r', encoding='utf-8') as input:
    input_lines = [i.split() for i in input.readlines()]
    merged_lists = []
    for word_list in input_lines:
        merged_lists.extend(word_list)

    for word in merged_lists:
        if len(word) == len(max(merged_lists, key=len)):
            print(word)
