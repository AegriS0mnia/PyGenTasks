m, n = int(input()), int(input())

books_in_shelf = {input() for i in range(m)}

for i in range(n):
    book = input()
    if book in books_in_shelf:
        print('YES')
    else:
        print('NO')

