scholar_number = int(input()) + int(input())
scholar = set()

for i in range(scholar_number):
    name = input()
    if name in scholar:
        scholar.discard(name)
    else:
        scholar.add(name)

print(len(scholar) if len(scholar) else 'NO')