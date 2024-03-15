last_name_1 = {i for i in input().split()}
last_name_2 = {j for j in input().split()}

print(*sorted(last_name_1 | last_name_2))
