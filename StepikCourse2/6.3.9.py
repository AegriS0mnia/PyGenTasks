students_number = int(input())
students_marks = []
nerds = []

for i in range(students_number):
    student_mark = input().split()

    students_marks.append(' '.join(student_mark))
    if int(student_mark[1]) >= 4:
        nerds.append(' '.join(student_mark))

print(*students_marks, sep='\n')
print()
print(*nerds, sep='\n')