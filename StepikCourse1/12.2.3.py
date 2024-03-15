line = [i for i in input().split()]

sum_ = '+'.join(line) + '=' + str(sum([int(i) for i in line]))

print(sum_)