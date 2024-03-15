line = input().split()
numbers_array = []
for L in line:
    numbers_array.append(int(L))

for j in numbers_array:
    print('+' * j, sep='\n')
