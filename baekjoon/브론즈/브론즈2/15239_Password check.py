def is_valid_password(word):
    str_set = '+_)(*&^%$#@!./,;{}'
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in word:
        if 'a' <= char <= 'z':
            has_lower = True
        if 'A' <= char <= 'Z':
            has_upper = True
        if '0' <= char <= '9':
            has_digit = True
        if char in str_set:
            has_special = True

    return has_lower and has_upper and has_digit and has_special and len(word) >= 12


for _ in range(int(input())):
    input()
    str_word = input()

    if is_valid_password(str_word):
        print('valid')
    else:
        print('invalid')
