counter_of_numbers = 0
counter_of_even_numbers = 0

for _ in range(10):
    number = int(input())
    counter_of_numbers += 1
    if number % 2 == 0:
        counter_of_even_numbers += 1

is_all_numbers_even = counter_of_numbers == counter_of_even_numbers

if is_all_numbers_even:
    print('YES')
else:
    print('NO')
