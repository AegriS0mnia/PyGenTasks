line = input().split()
line_copy = line
differ_indexes = [0] + [i for i in range(1, len(line) - 1) if line[i] != line[i-1]]

duplicates = []

for i in range(1, len(differ_indexes)):
    duplicates.append(line[differ_indexes[i-1]: differ_indexes[i]])

duplicates += [line[differ_indexes[-1]:]]

if duplicates[-1].count(duplicates[-1][0]) < len(duplicates[-1]):
    last_el = duplicates[-1][-1]
    duplicates[-1] = duplicates[-1][:-1]
    duplicates.append([last_el])

print(duplicates)
