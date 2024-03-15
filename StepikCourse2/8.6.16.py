number_of_numbers = int(input())

digits_in_common = set(input())
for _ in range(number_of_numbers - 1):
    digits_in_common = digits_in_common & set(input())

print(*sorted(digits_in_common))
