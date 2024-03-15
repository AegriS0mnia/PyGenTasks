number_of_numbers = int(input())
number_list = []
for i in range(number_of_numbers):
    number_list.append(int(input()))

product = int(input())

flag = False

for i in range(len(number_list)):
    if flag:
        print('ДА')
        break

    flag = False
    for j in range(len(number_list)):
        if number_list[i] * number_list[j] == product and i != j:
            flag = True
            break

if not(flag):
    print('НЕТ')