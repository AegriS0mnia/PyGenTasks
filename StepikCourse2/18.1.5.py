with open('18.1.7', 'r', encoding='utf-8') as file:
    file_lines = [line.strip() for line in file.readlines()[-10:]]

    print(*file_lines, sep='\n')
