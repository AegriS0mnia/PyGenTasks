first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number - 1, -1):
    if i % 2 != 0:
        print(i)
