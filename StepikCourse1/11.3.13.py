strings_number = int(input())
strings_list = []
new_string = ''
for i in range(strings_number):
    strings_list.append(input())
k = int(input())

for j in range(len(strings_list)):
    if len(strings_list[j]) >= k:
        new_string += str(strings_list[j])[k-1]

print(new_string)