line = input() + ' запретил букву'
letters = []

for i in line:
    if i not in letters:
        letters.append(i)
letters = sorted(letters)[1:]

while True:
    print(f'{line.strip()}  {letters[0]}'.replace('  ', ' '))
    line = line.replace(letters[0], '')

    if len(letters) != 1:
        letters = letters[1:]
    else:
        break
