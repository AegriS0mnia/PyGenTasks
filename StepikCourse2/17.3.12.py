with open('17.3.12.txt', 'r+', encoding='utf-8') as text:
    lines = text.readlines()
    lines_counter = len(lines)
    letters_counter = 0
    words_counter = 0

    for line in lines:
        while '  ' in line:
            line = line.strip().replace('  ', ' ')

        for j in line:
            if j.isalpha():
                letters_counter += 1

        words_counter += line.count(' ') + 1

print(f"""Input file contains:
 {letters_counter} letters
 {words_counter} words
 {lines_counter} lines""")
