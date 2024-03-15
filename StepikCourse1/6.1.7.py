dog_age = int(input())

if dog_age <= 2:
    human_age = 10.5 * dog_age
else:
    human_age = 21 + 4*(dog_age - 2)

print(human_age)