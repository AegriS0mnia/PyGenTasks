number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

middle_number = 0
local_max = number_1
local_min = number_2

if number_2 > local_max:
    local_max = number_2
    local_min = number_1

if number_3 > local_max:
    middle_number = local_max
elif number_3 < local_max:
    if number_3 > local_min:
        middle_number = number_3
    else:
        middle_number = local_min


print(middle_number)