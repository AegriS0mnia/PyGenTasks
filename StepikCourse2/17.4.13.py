number_of_files = int(input())

with open('17.4.9.outputfile', 'w', encoding='utf-8') as output_file:
    files_names = [input() for i in range(number_of_files)]

    for i in range(number_of_files):
        with open(files_names[i], 'r', encoding='utf-8') as current_input:
            input_lines = current_input.readlines()
            output_file.writelines([f'{line}' for line in input_lines])

