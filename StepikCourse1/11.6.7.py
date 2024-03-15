line = input().lower().split()
counter = line.count('a') + line.count('an') + line.count('the')

print(f'Общее число артиклей: {counter}')
