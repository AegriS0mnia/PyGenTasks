with open('first_names.txt', 'r+', encoding='utf-8') as names, open('last_names.txy', 'r+', encoding='utf-8') as last_names:
    names = set(names.read().split())
    last_names = set(last_names.read().split())

    for i in range(3):
        print(f'{names.pop()} {last_names.pop()}')
