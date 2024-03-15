from math import  factorial


def compute_binom(n, k):
    binom = int(factorial(n) / (factorial(k) * factorial(n - k)))

    print(binom)


n, k = int(input()), int(input())

compute_binom(n,k)