number = int(input())

array = [list(range(1, number + 1)) for i in range(1, number + 1)]

print(*array, sep='\n')