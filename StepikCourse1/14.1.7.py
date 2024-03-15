def number_to_words(number):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if 10 < number < 20:
        print(teens[number % 10 - 1])
    elif 1 <= number < 10:
        print(units[number % 10])
    elif number == 10:
        print('десять')
    else:
        print(f'{tens[number // 10 - 2]} {units[number % 10]}'.rstrip())


number = int(input())

number_to_words(number)