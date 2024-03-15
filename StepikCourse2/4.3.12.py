line = input().split()

counter = 1
duplicates = []
numbers_set = []
flag = True

for i in line:
    if i not in numbers_set:
        numbers_set.append(i)

for i in range(1, len(line)):
    if len(line) == line.count(line[0]):
        print([line])
        flag = False
        break
    if len(line) == len(numbers_set):
        line = [[i] for i in line]
        print(line)
        flag = False
        break

    if line[i - 1] == line[i]:
        counter += 1
    else:
        duplicates.append(list(line[i - 1] * counter))
        counter = 1

if line[-2] == line[-1] and flag:
    duplicates.append(line[-2:])
    print(duplicates)
elif line[-2] != line[-1] and flag:
    duplicates.append([line[-1]])
    print(duplicates)


