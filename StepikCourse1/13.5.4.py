from math import ceil

def is_prime(number):
    is_number_prime = True
    factors = []

    if number == 1:
        return False
    for i in range(1,  ceil(number**0.5) + 1):
        if number % i == 0 and i not in factors:
            factors.append(i)
            factors.append(number // i)
        if len(factors) > 2:
            is_number_prime = False
            break
    return is_number_prime

def get_next_prime(number):
    next_prime = number + 1
    if is_prime(next_prime):
        return  next_prime
    else:
        while not(is_prime(next_prime)):
            next_prime += 1

    return next_prime

number = int(input())


print(get_next_prime(number))