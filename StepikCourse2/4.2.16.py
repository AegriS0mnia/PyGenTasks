list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

def list_sum(list1):
    total = 0
    counter = 0
    for li in list1:
        for j in li:
            total += j
            counter += 1
    mean = total / counter
    return mean

print(list_sum(list1))
