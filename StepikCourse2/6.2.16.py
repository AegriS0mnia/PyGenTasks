tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [tup[:len(tup) - 1] + (100,) for tup in tuples]

print(new_tuples)
