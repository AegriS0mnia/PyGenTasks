number_of_files = int(input())

lines = [input().split() for i in range(number_of_files)]
files = {i[0]: i[1:] for i in lines}

for key in files:
    if 'W' in files[key]:
        files[key][files[key].index('W')] = 'write'
    if 'X' in files[key]:
        files[key][files[key].index('X')] = 'execute'
    if 'R' in files[key]:

        files[key][files[key].index('R')] = 'read'

number_of_requests = int(input())

requests = [input().split() for i in range(number_of_requests)]
requests_reversed = [(i[1], i[0]) for i in requests]

for request in requests_reversed:
    if request[0] in files and request[1] in files[request[0]]:
        print('OK')
    else:
        print('Access denied')