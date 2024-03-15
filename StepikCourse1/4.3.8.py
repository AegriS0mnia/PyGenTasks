first_operand = int(input())
second_operand = int(input())
operation_symbol = input()

if operation_symbol == '/':
    if second_operand != 0:
        print(first_operand / second_operand)
    else:
        print('На ноль делить нельзя!')
elif operation_symbol == '+':
    print(first_operand + second_operand)
elif operation_symbol == '-':
    print(first_operand - second_operand)
elif operation_symbol == '*':
    print(first_operand * second_operand)
else:
    print('Неверная операция')

