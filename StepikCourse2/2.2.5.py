unique_elements = []

numbers = [int(i) for i in input().split() if i not in unique_elements]

for i in numbers:
    if i not in unique_elements:
        unique_elements.append(i)

print(len(unique_elements))
