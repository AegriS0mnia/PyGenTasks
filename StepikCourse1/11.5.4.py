full_name = input().split()
initials_list = []

for n in full_name:
    initials_list.append(n[0])

initials = '.'.join(initials_list) + '.'

print(initials)
