def interesting_numbers(a, b):
    interesting_numbers = []

    numbers_without_0 = [i for i in range(a, b + 1) if '0' not in str(i)]

    for number in numbers_without_0:
        if all(map(lambda divider: number % divider == 0, get_digits(number))):
            interesting_numbers.append(number)

    return interesting_numbers


def get_digits(number):
    digits = [int(i) for i in str(number)]

    return digits


a, b = int(input()), int(input())


print(*interesting_numbers(a, b))
