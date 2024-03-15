first_term = int(input())
second_term = int(input())
third_term = int(input())

condition_of_progression = second_term - first_term == third_term - second_term

if condition_of_progression: 
    print("YES")
else:
    print("NO")