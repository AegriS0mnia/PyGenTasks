line1 = sorted([i.lower() for i in input() if i.isalpha()])
line2 = sorted([i.lower() for i in input() if i.isalpha()])

print('YES' if line1 == line2 else 'NO')

