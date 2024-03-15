cubes_number = int(input())
cubes_list = []

for _ in range(cubes_number):
    cubes_list.append(int(input())**3)

print(cubes_list)