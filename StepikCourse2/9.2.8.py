num1, num2 = int(input()), int(input())

math = {input() for i in range(num1)}
cs = {input() for i in range(num2)}

math_only = math - (math & cs)

print(len(math_only))