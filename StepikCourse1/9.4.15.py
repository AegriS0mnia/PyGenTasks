text = input()

new_text = text[:text.find('h')] + text[text.rfind('h') + 1:]

print(new_text)