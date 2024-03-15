def is_password_good(password):
    len_check = len(password) >= 8
    valid_symbols_check = password.isalnum() and not(password.isdigit() or password.isalpha())
    capitals_lowercase_check = (password.swapcase() != password.upper()) and (password.swapcase() != password.lower())
    password_check = len_check and valid_symbols_check and capitals_lowercase_check
    return password_check

password = input()

print(is_password_good(password))