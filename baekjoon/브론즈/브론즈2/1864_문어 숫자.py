mapping = {
    '-': 0, '\\': 1, '(': 2, '@': 3,
    '?': 4, '>': 5, '&': 6, '%': 7,
    '/': -1
}

while 1:
    s = input()
    if s == '#':
        exit()
    result = 0
    length = len(s)
    for i, ch in enumerate(s):
        value = mapping[ch]
        power = length - i - 1
        result += value * (8 ** power)
    print(result)
