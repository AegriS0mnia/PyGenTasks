def quick_merge(list):
    return sorted(list)


list = []

for i in range(int(input())):
    for j in input().split():
        list.append(int(j))


print(*quick_merge(list))
