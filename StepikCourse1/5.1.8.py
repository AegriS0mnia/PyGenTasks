X1, Y1 = int(input()), int(input())
X2, Y2 = int(input()), int(input())

queen_move = (X2 - X1 == 0 or Y2 - Y1 == 0) or ((X2 - X1)**2 == (Y2 - Y1)**2)
if queen_move:
    print('YES')
else:
    print('NO')
