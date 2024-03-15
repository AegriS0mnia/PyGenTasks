line = input().split()
counter = 0
for i in range(len(line)):
    for j in line:
        if int(j) == int(line[i]):
            counter += 1
counter = (counter - len(line)) // 2

print(counter)
