def ip_check(possible_ip):
    is_ip_correct = all(map(lambda digits: digits.isdigit() and 0 <= int(digits) <= 255, possible_ip.split('.')))

    return is_ip_correct


possible_ip = input()


print(ip_check(possible_ip))
