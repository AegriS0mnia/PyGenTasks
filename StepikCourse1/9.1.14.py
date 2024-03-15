text = input()

VOWELS = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
CONSONANTS = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
vowels_counter = 0
consonants_counter = 0

for c in text:
    if c in VOWELS:
        vowels_counter += 1
    if c in CONSONANTS:
        consonants_counter += 1

print('Количество гласных букв равно', vowels_counter)
print('Количество согласных букв равно', consonants_counter)