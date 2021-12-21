password = input("Enter the password:")

length = len(password)
recommend = ''
if length < 12:
    recommend += f'increase the number of characters - {12 - length}, '
if not any(map(str.isupper, password)):
    recommend += 'add 1 capital letter, '
if not any(map(str.islower, password)):
    recommend += 'add 1 lowercase letter, '
if not any(map(str.isdigit, password)):
    recommend += 'add 1 digit, '
is_spec = any(symbol in '!@#$%^&*()-+' for symbol in password)
if not is_spec:
    recommend += 'add 1 special character, '
if not password.isalnum() and not is_spec:
    print(f'Error, Forbidden character')
else:
    if len(recommend) == 0:
        print('Strong password')
    else:
        print(f'Weak password. Recommendations: {recommend[:-2]}.')
