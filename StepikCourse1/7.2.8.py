first_number = int(input())
second_number = int(input())

if first_number > second_number:
    for i in range(first_number, second_number - 1, -1):
        print(i)
elif first_number < second_number:
    for i in range(first_number, second_number + 1):
        print(i)
else:
    print(first_number)
