line = input().split()

for _ in line:
    line.append(int(line[0]))
    line = line[1:]

line.sort()

print(*line)
print(*line[::-1])