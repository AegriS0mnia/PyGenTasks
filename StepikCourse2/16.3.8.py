from operator import mul
from operator import truediv
from operator import add
from operator import sub

def arithmetic_operation(operator):
    operations = {'*': mul, '/': truediv, '+': add, '-': sub}
    return operations[operator]

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))