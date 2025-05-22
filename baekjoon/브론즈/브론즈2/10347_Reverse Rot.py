alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while 1:
    line = input()
    if len(line) < 2:
        exit()
    parts = line.split(' ', 1)
    n, message = int(parts[0]), parts[1]

    for ch in message[::-1]:
        idx = alphabet.index(ch)
        new_idx = (idx + n) % len(alphabet)
        print(alphabet[new_idx], end='')

    print()
