with open('17.3.10', 'r+', encoding='utf-8') as numbers:
    for line in numbers:
        sum_ = sum([int(j) for j in line.split() if j.isdigit()])
        print(sum_)
