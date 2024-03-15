ip = input().split('.')

is_ip_valid = 'ДА'

for i in ip:
    if int(i) < 0 or int(i) > 255:
        is_ip_valid = 'НЕТ'

print(is_ip_valid)