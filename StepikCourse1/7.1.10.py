population = int(input())
daily_increase = int(input())
days_to_breed = int(input())

for i in range(days_to_breed):
    print(i + 1, population)
    population *= (1 + daily_increase / 100)
