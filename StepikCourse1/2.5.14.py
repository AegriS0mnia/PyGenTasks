number = int(input())

a = number // 100  # сотни
b = number // 10 % 10  # десятки
c = number % 10  # единицы

abc = number
acb = a*100 + c*10 + b
bac = b*100 + a*10 + c
bca = b*100 + c*10 + a
cab = c*100 + a*10 + b
cba = c*100 + b*10 + a

print(abc, acb, bac, bca, cab, cba, sep='\n')