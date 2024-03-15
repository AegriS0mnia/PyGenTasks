number = int(input())

sum_of_even = 0

while number != 0:
    if number % 2 != 1:
        sum_of_even += number % 10
    number //= 10

print(sum_of_even)
