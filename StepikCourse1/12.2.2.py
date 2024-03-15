L = [int(i) for i in input().split()]
M = [int(j) for j in input().split()]
K = []
for k in range(len(L)):
    K.append(L[k] + M[k])

print(*K)