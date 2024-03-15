sdwvig = int(input())
text = input()

for i in text:
    if ord(i) - sdwvig > ord('a'):
        print(chr(ord(i) - sdwvig), end='')
    else:
        print(chr(ord(i) + sdwvig), end='')