line = input().split()

sub_lists = []
start_index = 0
for i in range(len(line) + 1):
    start_index = 0

    for j in range(len(line) - i + 1):
        sub_list = line[start_index: start_index + i]
        start_index += 1
        if sub_list not in sub_lists or len(sub_list) <= 1:
            sub_lists.append(sub_list)

while sub_lists.count([]) > 1:
    del sub_lists[0]

print(sub_lists)
