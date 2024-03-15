text = input()

new_text = text[:text.find('h') + 1] + text[text.find('h') + 1:text.rfind('h')][::-1] + text[text.rfind('h'):]

print(new_text)