X1, Y1 = int(input()), int(input())
X2, Y2 = int(input()), int(input())

bishop_move = (X2 - X1)**2 == (Y2 - Y1)**2

if bishop_move:
    print('YES')
else:
    print('NO')