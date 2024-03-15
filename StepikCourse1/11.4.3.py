number_of_numbers = int(input())
argument_set = []
function_value_set = []

for _ in range(number_of_numbers):
    argument = int(input())
    function_value = argument**2 + 2*argument + 1
    argument_set.append(argument)
    function_value_set.append(function_value)

print(*argument_set, sep='\n')
print()
print(*function_value_set, sep='\n')