while 1:
    s = input()
    if s == '0':
        exit()

    encoded = []
    count = 1
    current = s[0]

    for ch in s[1:]:
        if ch == current:
            count += 1
        else:
            encoded.append(count)
            encoded.append(current)
            current = ch
            count = 1

    encoded.append(count)
    encoded.append(current)

    print(*encoded, sep='')
