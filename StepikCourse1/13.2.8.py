from math import  ceil

def draw_triangle(fill, base):
    for i in range(1, base + 1):
        if i <= base // 2 + base % 2:
            print(fill * i)
        else:
            print(fill * (base - i + 1))

fill = input()
base = int(input())


draw_triangle(fill, base)