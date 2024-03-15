def is_palindrome(text):
    clear_string = ''
    for c in text:
        if c.isalpha():
            clear_string += c
    palindrome_check = clear_string == clear_string[::-1]

    return palindrome_check

text = input().lower()


print(is_palindrome(text))