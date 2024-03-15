X1, Y1 = int(input()), int(input())
X2, Y2 = int(input()), int(input())

king_move = (X2 - X1)**2 <= 1 and (Y2 - Y1)**2 <= 1

if king_move:
    print('YES')
else:
    print('NO')