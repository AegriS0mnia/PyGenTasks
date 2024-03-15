countries_quantity = int(input())

dictionary_of_countries = {}

for i in range(countries_quantity):
    country = tuple(input().split())
    dictionary_of_countries.setdefault(country[1:], country[0])

query_quantity = int(input())

for i in range(query_quantity):
    query = input()
    for key in dictionary_of_countries:
        if query in key:
            print(dictionary_of_countries[key])
