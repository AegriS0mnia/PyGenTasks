marks1 = set(int(i) for i in input().split())
marks2 = set(int(i) for i in input().split())
marks3 = set(int(i) for i in input().split())

print(*sorted(set(range(11)) - (marks1 | marks2 | marks3)))

