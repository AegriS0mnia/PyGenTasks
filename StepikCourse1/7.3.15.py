number_of_terms = int(input())

a_previous, a_current = 0, 1

if number_of_terms == 1:
    print(1)
else:
    print(1, end=' ')
    for _ in range(number_of_terms - 1):
        a_next = a_previous + a_current
        print(a_next, end=' ')
        a_previous = a_current
        a_current = a_next
