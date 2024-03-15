from random import choice

number_of_friends = int(input())

friend_list = [input() for i in range(number_of_friends)]

result = []

used_friends = []

while len(result) < number_of_friends:
    