password = input("Введите пароль: ")

lenght = len(password)
recomend = ''
if lenght < 12:
    recomend += f'увеличить число символов - {12 - lenght}, '
if not any(map(str.isupper, password)):
    recomend += 'добавить 1 заглавную букву, '
if not any(map(str.islower, password)):
    recomend += 'добавить 1 строчную букву, '
if not any(map(str.isdigit, password)):
    recomend += 'добавить 1 цифру, '
isspec = any(simbol in '!@#$%^&*()-+' for simbol in password)
if not isspec:
    recomend += 'добавить 1 спецсимвол, '
if not password.isalnum() and not isspec:
    print(f'Ошибка, Запрещенный символ')
else:
    if len(recomend) == 0:
        print('Сильный пароль')
    else:
        fin_len = len(recomend)
        print(f'Слабый пароль. Рекомендации: {recomend[: fin_len - 2]}.')


