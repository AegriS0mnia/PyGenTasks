number = int(input())

five_counter = 0

while 0 < number <= 5:
    if number == 5:
        five_counter += 1
    number = int(input())

print(five_counter)
