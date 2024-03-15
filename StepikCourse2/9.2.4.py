number_of_citites = int(input())

cities = {input() for i in range(number_of_citites)}

city = input()

print('REPEAT' if city in cities else 'OK')