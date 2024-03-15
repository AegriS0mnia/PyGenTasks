def mean(*args):
    numbers = []

    for i in args:
        if type(i) == float or type(i) == int:
            numbers.append(i)

    if len(numbers) != 0:
        return sum(numbers) / len(numbers)
    else:
        return 0.0
