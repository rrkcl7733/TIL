lst = ['a', 'e', 'i', 'o', 'u']


def f(password):
    for i in lst:
        if i in password:
            break
    else:
        return 'not '
    for i in range(len(password) - 2):
        if password[i] in lst and password[i + 1] in lst and password[i + 2] in lst:
            return 'not '
        elif not (password[i] in lst) and not (password[i + 1] in lst) and not (password[i + 2] in lst):
            return 'not '
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            if password[i] in ('e', 'o'):
                continue
            else:
                return 'not '
    return ''


while 1:
    password = input()
    if password == 'end':
        exit()
    ans = f(password)
    print(f'<{password}> is ' + ans + 'acceptable.')
