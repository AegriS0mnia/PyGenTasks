bottom_line = int(input())
upper_bound = int(input())

counter = 0

for i in range(bottom_line, upper_bound + 1):
    if i**3 % 10 == 4 or i**3 % 10 == 9:
        counter += 1

print(counter)
