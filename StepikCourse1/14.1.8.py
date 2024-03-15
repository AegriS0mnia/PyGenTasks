def get_month(lang, number):
    months_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    months_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if lang == 'ru':
        print(months_ru[number - 1])
    else:
        print(months_en[number - 1])


lang = input()
number = int(input())

get_month(lang, number)