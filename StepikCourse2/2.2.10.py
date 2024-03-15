for n in range(1, int(input()) + 1):
    code = input()
    code = code[code.find('a'):]
    a = code.find('a')
    t = code.find('t')
    o = code.find('o')
    n1 = code.find('n')
    n2 = code.rfind('n')
    if (n1 != n2 and n1 < t) and str(code[0] + code[n1] + code[t] + code[o] + code[n2]) == 'anton':
        print(n, end=' ')