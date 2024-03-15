string = input()
counter = 0

for i in range(1, len(string)):
    if string[i - 1] == string[i]:
        counter += 1

print(counter)
