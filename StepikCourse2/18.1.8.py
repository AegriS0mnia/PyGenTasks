with open('18.1.8', 'r', encoding='utf-8') as code:
    code_lines = code.readlines()
    flag = True
    for i in range(1, len(code_lines)):
        current_line = code_lines[i]
        previous_line = code_lines[i - 1]

        if 'def ' in current_line and '#' not in previous_line:
            print(current_line[current_line.find(' ') + 1: current_line.find('(')])
            flag = False
        elif i == 1 and previous_line.startswith('def '):
            print(previous_line[previous_line.find(' ') + 1: previous_line.find('(')])
            flag = False

    if flag:
        print('Best Programming Team')
