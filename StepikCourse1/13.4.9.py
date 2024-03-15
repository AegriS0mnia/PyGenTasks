def get_factors(num):
    factors = [i for i in range(1, num //2 +1) if num % i == 0] + [num]
    return factors

def number_of_factors(num):
    return len(get_factors(num))

num = int(input())


print(number_of_factors(num))