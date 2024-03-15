text = input()

if text.count('f') == 0:
    print(-2)
elif text.count('f') == 1:
    print(-1)
else:
    print((text.replace('f', '', 1,).find('f')) + 1)