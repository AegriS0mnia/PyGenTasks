n = int(input())
b = str()
while n != 0:
    a = n % 2
    b = str(a) + b
    n = n // 2
print(b)
