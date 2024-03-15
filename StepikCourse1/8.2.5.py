number = input()

third_digit = int(number) // 10**(len(number) - 3) % 10

print(third_digit)
