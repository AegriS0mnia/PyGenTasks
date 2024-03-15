text = input()

if text.find('f') == - 1:
    print('NO')
elif text.find('f') == text.rfind('f'):
    print(text.find('f'))
else:
    print(text.find('f'), text.rfind('f'))