for i in range(int(input())):
    special_chars = "#@*&"
    input()
    password = input()
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in special_chars for c in password)

    if not uppercase:
        password += 'A'
    if not lowercase:
        password += 'a'
    if not digit:
        password += '0'
    if not special:
        password += '#'

    while len(password) < 7:
        password += 'A'

    print(f'Case #{i + 1}: {password}')
