def check_password(password):
    is_password_good = len(password) >= 7 and password.lower() != password != password.upper() and not(password.isalpha()) and password.isalnum()

    return 'YES' if is_password_good else 'NO'


password = input()

print(check_password(password))
