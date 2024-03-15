numbers = input().split()

print(f"{numbers[-1]} {' '.join(numbers[: len(numbers) - 1])}")