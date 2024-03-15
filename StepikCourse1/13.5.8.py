from math import ceil


def is_prime(number):
    is_number_prime = True
    factors = []

    if number == 1:
        return False
    for i in range(1, ceil(number ** 0.5) + 1):
        if number % i == 0 and i not in factors:
            factors.append(i)
            factors.append(number // i)
        if len(factors) > 2:
            is_number_prime = False
            break
    return is_number_prime


def is_valid_password(password):
    password_check = len(password) == 3 and password[0] == password[0][::-1] and is_prime(number) and int(password[2]) % 2 == 0
    return password_check


password = [i for i in input().split(':')]
number = int(password[1])

print(is_valid_password(password))


