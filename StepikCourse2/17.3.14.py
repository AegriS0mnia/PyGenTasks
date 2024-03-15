with open('17.3.14', 'r+', encoding='utf-8') as population:
    data = [country.split() for country in population.readlines()]
    filtered_data = filter(lambda country: country[0][0] == 'G' and int(country[-1]) > 5*10**5, data)

    for country in filtered_data:
        print(country[0])
