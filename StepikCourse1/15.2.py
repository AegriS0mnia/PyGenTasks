import random


def is_valid_number(user_input):
    valid_check = user_input.isdigit() and 1 <= int(user_input) <= 100
    return valid_check


def greeting():
    GREETING = 'Привет, давай сыграем в игру'
    RULES = 'Я загадаю число от 1 до 100, а ты попытайся его отгадать'

    print(GREETING, RULES, sep='\n')

def generate_number(right_bound):
    number = random.randrange(1, right_bound)
    return number
def number_choice():

    NUMBER = generate_number()

    while True:
        user_input = input()

        if is_valid_number(user_input):
            user_input = int(user_input)
            if user_input > NUMBER:
                print('Слишком много, попробуйте ещё раз')
                continue
            elif user_input < NUMBER:
                print('Слишком мало, попробуйте ещё раз')
                continue
            else:
                print('Вы угадали, поздравляем!')
                break
        else:
            print('А может всё-таки ввёдешь целое число от 1 до 100?')

def game():
    number_choice()



