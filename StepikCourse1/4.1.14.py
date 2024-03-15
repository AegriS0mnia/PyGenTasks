X1, Y1 = int(input()), int(input())
X2, Y2 = int(input()), int(input())

rook_move = X2-X1 == 0 or Y2-Y1 == 0

if rook_move:
    print('YES')
else:
    print('NO')