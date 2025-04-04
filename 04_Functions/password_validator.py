def is_valid_password(string):
    is_valid = True
    if len(string) < 6 or len(string) > 10:
        print('Password must be between 6 and 10 characters')
        is_valid = False
    if not password.isalnum():
        print('Password must consist only of letters and digits')
        is_valid = False
    counter_digits = 0
    for character in string:
        if character.isdigit():
            counter_digits += 1
    if counter_digits < 2:
        print('Password must have at least 2 digits')
        is_valid = False
    return is_valid


password = input()
password_is_valid = is_valid_password(password)
if password_is_valid:
    print('Password is valid')
