a1, b1 = int(input()), int(input())
a2, b2 = int(input()), int(input())

one_common_point_1 = a1 < a2 and a2 == b1
one_common_point_2 = a1 > a2 and a1 == b2

if one_common_point_1:
    print(a2)
elif one_common_point_2:
    print(a1)
elif a2 > a1 and b2 < b1:
    print(a2, b2)
elif a1 == a1 and b2 < b1:
    print(a1, b2)
elif a1 == a1 and b2 > b1:
    print(a2, b1)
elif a2 > a1 and b1 == b2:
    print(a2, b1)
elif a2 < a1 and b1 == b2:
    print(a1, b2)


elif a2 > a1 and b2 > b1 and a2 < b1:
    print(a2, b1)
elif a2 < a1 and b2 < a1 and b2 > a1:
    print(a1, b2)
else:
    print('пустое множество')