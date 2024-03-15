m, n = int(input()), int(input())

for i in range(m, n + 1):
    number_check = i % 17 == 0 or i % 10 == 9 or i % 15 == 0
    if number_check:
        print(i)
