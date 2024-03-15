def is_correct_bracket(text):
    answer = True

    if text.count('(') == text.count(')'):
        while text.strip() != '' or text == ' ':
            if text.find('(') < text.find(')'):
                text = text.replace('(', '', 1)
                text = text.replace(')', '', 1)
                text = text.replace(' ', '')
                continue
            else:
                answer = False
            if answer == False:
                break
    else:
        answer = False
    return answer


text = input()

print(is_correct_bracket(text))