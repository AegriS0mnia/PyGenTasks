def check_excellent_student(list_of_students):
    is_nerd_in_each_class = all(map(lambda students_sheet: '5' in students_sheet, list_of_students))

    return 'YES' if is_nerd_in_each_class else 'NO'


def input_students_info(number_of_classes):
    list_of_students = []

    for _ in range(number_of_classes):
        students = ''
        number_of_students = int(input())

        for _ in range(number_of_students):
            students += ' ' + input() + ''
        list_of_students.append(students)

    return list_of_students


number_of_classes = int(input())

list_of_students = input_students_info(number_of_classes)

print(check_excellent_student(list_of_students))

