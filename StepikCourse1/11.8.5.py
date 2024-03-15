_list = [99, 4, 5, 68, 8, 3, 2, 1]

for i in range(len(_list) - 1):
    _list[-1 - i], _list[i] = max(_list[:len(_list) - i  -1],, _list[-1 - i]

print(_list)