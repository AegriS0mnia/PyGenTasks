def is_magic(date):
    magic_check = date[0] * date[1] == date[2] % 100
    return magic_check


date = [int(i) for i in input().split('.')]

print(is_magic(date))
