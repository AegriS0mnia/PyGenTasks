number = int(input())

for i in range(1, number//2 + 2):
    print('*' * i)
for j in range(number // 2, 0, -1):
    print('*' * j)