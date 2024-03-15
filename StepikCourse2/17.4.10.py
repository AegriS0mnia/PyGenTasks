with open('17.4.10', 'r', encoding='utf-8') as input, open('17.4.10out', 'w', encoding='utf-8') as output:
    input_lines = input.readlines()

    for index, line in enumerate(input_lines, 1):
        print(f'{index}) {line}', file=output, end='')
