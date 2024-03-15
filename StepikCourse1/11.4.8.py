numbers = [int(input()) for i in range(int(input()))]

negatives = [i for i in numbers if i < 0]
zeros = [i for i in numbers if i == 0]
positives = [i for i in numbers if i > 0]

sorted_number = negatives + zeros + positives

print(*sorted_number, sep='\n')
