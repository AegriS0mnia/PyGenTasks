number_of_messages = int(input())
count = 0

for _ in range(number_of_messages):
    message = input()
    if message.count('11') >= 3:
        count += 1

print(count)