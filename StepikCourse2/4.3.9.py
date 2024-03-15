number = int(input())

array = []
for i in range(1, number + 1):
    row = []

    for j in range(1, i + 1):
        row.append(j)
    array.append(row)

print(*array, sep='\n')