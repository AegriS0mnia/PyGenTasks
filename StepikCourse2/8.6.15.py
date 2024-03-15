numbers1 = set(int(i) for i in input().split())
numbers2 = set(int(i) for i in input().split())

print(*sorted(numbers1 - numbers2))
