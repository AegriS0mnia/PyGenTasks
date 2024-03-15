def to_camel_case(text):
    if '_' in text:
        text = text.split('_')
    else:
        text = text.split('-')

    line = [text[0]] + ([i.capitalize() for i in text[1:]])
    line = ''.join(line)
    return line

