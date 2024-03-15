counter = 0
flag = False
for i in range(1, 35):
    if flag:
        break
    for j in range(1, 35):
        for z in range(1, 35):
            for g in range(1, 35):
                if i != j and i != z and i != g and j != z and j != g and z != g:
                    if i**3 + j**3 == z**3 + g**3:
                        print(i**3 + j**3)
                        counter += 1
                    if counter == 7:
                        flag = True