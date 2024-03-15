countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

info = list(zip(capitals, countries, population))

for city in info:
    print(f'{city[0]} is the capital of {city[1]}, population equal {int(city[2])} people.')


