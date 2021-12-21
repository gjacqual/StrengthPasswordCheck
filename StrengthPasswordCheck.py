password = input("Enter the password:")

lenght = len(password)
recomend = ''
if lenght < 12:
    recomend += f'increase the number of characters - {12 - lenght}, '
if not any(map(str.isupper, password)):
    recomend += 'add 1 capital letter, '
if not any(map(str.islower, password)):
    recomend += 'add 1 lowercase letter, '
if not any(map(str.isdigit, password)):
    recomend += 'add 1 digit, '
isspec = any(simbol in '!@#$%^&*()-+' for simbol in password)
if not isspec:
    recomend += 'add 1 special character, '
if not password.isalnum() and not isspec:
    print(f'Error, Forbidden character')
else:
    if len(recomend) == 0:
        print('Strong password')
    else:
        fin_len = len(recomend)
        print(f'Weak password. Recommendations: {recomend[: fin_len - 2]}.')


