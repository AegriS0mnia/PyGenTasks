num1, num2 = int(input()), int(input())

math = {input() for i in range(num1)}
cs = {input() for i in range(num2)}

one_subject_only = len(math ^ cs)

print(one_subject_only if one_subject_only else 'NO')