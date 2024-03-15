numbers = input().split()
numbers_set = set()

for i in numbers:
    print('YES' if int(i) in numbers_set else 'NO')
    numbers_set.add(int(i))
