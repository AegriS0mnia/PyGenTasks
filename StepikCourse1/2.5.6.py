first_term = int(input())
denominator = int(input())
number_of_nth_term = int(input())

nth_term = first_term*denominator**(number_of_nth_term-1)

print(nth_term)