def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number='17'):
    if mail is not None:
        return (f"""To: {mail}
Приветствую, {name}!
Вам назначен экзамен, который пройдет {date}, в {time}.
По адресу: {place}. 
Экзамен будет проводить {teacher} в кабинете {number}. 
Желаем удачи на экзамене!""")
    else:
        return " "
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
