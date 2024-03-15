phones_quantity = int(input())
lines = [input().split() for i in range(phones_quantity)]

friends = dict((friend[1].lower(), None) for friend in lines)

for friend in friends:
    phones = []
    for line in lines:
        if friend in line[1].lower():
            phones.append(line[0])

    friends[friend] = phones

queries_quantity = int(input())

print(friends)

for i in range(queries_quantity):
     query = input().lower()
     if query in friends:
         print(friends[query])
     elif query not in friends:
         print('абонент не найден')