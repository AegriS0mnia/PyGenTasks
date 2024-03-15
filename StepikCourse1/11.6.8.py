lines_number = int(input()[1:])
lines = []

for _ in range(lines_number):
    line = input()
    if '#' in line:
        line = line[:line.find('#')].rstrip()
    lines.append(line)

print(*lines, sep='\n')