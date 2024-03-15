city1, city2, city3 = input(), input(), input()

city1_len, city2_len, city3_len = len(city1), len(city2), len(city3)

min_len = min(city1_len, city2_len, city3_len)
max_len = max(city1_len, city2_len, city3_len)

if city1_len == min_len:
    print(city1)
elif city2_len == min_len:
    print(city2)
else:
    print(city3)

if city1_len == max_len:
    print(city1)
elif city2_len == max_len:
    print(city2)
else:
    print(city3)