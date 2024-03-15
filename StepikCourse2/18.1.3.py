with open('grades.txt', 'r', encoding='utf-8') as grades:
    counter = 0
    grades_lines = grades.readlines()
    for students_grades in grades_lines:
        students_grades = students_grades.split()
        if all(map(lambda mark: int(mark) >= 65, students_grades[1:])):
            counter += 1
    print(counter)
