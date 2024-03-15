number_of_terms = int(input())

max_pomenshe = -1
max_bolshoi = -1

for _ in range(number_of_terms):
    number = int(input())
    max_pomenshe, max_bolshoi = min(max(max_pomenshe, number), max_bolshoi), max(max_bolshoi, number)


print(max_bolshoi, max_pomenshe, sep='\n')
