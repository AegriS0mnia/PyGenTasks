numbers = [int(i) for i in input().split()]
last_element = []
zigzag = []

if len(numbers) % 2:
    last_element = numbers[-1]
else:
    last_element = ''

for i in range(len(numbers) // 2):
    zigzag.append(numbers[:2][::-1])
    numbers = numbers[2:]

for i in zigzag:
    print(*i, end=' ')

print(last_element)
