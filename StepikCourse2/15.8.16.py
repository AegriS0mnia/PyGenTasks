def evaluate():
    sum = 0
    for i in range(len(coefficients)):
        sum += coefficients[i] * argument**pows[i]

    return sum


coefficients = [int(i) for i in input().split()]
argument = int(input())
pows = list(range(len(coefficients)))[::-1]

print(evaluate())