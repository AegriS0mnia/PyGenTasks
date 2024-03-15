def delete_letters(line):
    new_line = line
    for i in new_line:
        if i.isalpha():
            while i in new_line:
                new_line = new_line.replace(i, ' ')

    return new_line


with open('17.3.11', 'r+', encoding='utf-8') as numbers:
    sum_ = 0
    for line in numbers:
        line = delete_letters(line)
        sum_ += sum([int(j) for j in line.split() if j.isdigit()])

    print(sum_)
