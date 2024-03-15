a, b = int(input()), int(input())

max_sum = 1
current_max = 1
this_number = 1

for number in range(a, b + 1):
    current_max = 0
    for divider in range(1, number + 1):
        if number % divider == 0:
            current_max += divider
        if current_max >= max_sum:
            max_sum = max(max_sum, current_max)
            this_number = number


print(this_number, max_sum)


