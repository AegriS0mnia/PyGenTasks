number = input()

numeric_root = number

while int(number) >= 10:
    numeric_root = 0
    for i in number:
        numeric_root += int(i)

    number = str(numeric_root)

print(numeric_root)
