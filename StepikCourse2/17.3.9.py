with open('17.3.9', 'r+', encoding='utf-8') as text:
    lines = [line.strip() for line in text.readlines()]
    max_line_len = len(max(lines, key=len))
    print(*filter(lambda line: len(line) == max_line_len, lines), sep='\n')
