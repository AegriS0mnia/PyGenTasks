with open('17.3.8', 'r+', encoding='utf-8') as text:
    reversed_lines = [line.strip() for line in text][::-1]
    print(*reversed_lines, sep='\n')
