letters_number = int(input())
alpha = ''

for i in range(97, 97 + letters_number):
    alpha += chr(i)

print(list(alpha))