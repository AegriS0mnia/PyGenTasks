DNA = input().upper()

adenine = 0
guanine = 0
cytosine = 0
thymine = 0

for c in DNA:
    if c == 'А':
        adenine += 1
    elif c == 'Г':
        guanine += 1
    elif c == 'Ц':
        cytosine += 1
    elif c == 'Т':
        thymine += 1
    else:
        continue

print('Аденин:', adenine)
print('Гуанин:', guanine)
print('Цитозин:', cytosine)
print('Тимин:', thymine)