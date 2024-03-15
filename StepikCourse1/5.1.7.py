X1, Y1 = int(input()), int(input())
X2, Y2 = int(input()), int(input())

horse_move = (abs(X2-X1) == 1 and abs(Y2-Y1) == 2) or (abs(X2-X1) == 2 and abs(Y2-Y1)== 1)

if horse_move:
    print('YES')
else:
    print('NO')