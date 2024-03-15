text = input()

current_max = 1
abs_max = 1
most_frequent = text[0]

for i in range(1, len(text)):
    if text[i - 1] == text[i]:
        current_max += 1
    else:
        current_max = 1
    if current_max >= abs_max:
        abs_max = current_max
        most_frequent = text[i]

print(most_frequent)
