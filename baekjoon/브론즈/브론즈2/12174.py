def google(s):
    for i in range(0, len(s), 8):
        a = 0
        t = 2 ** 7

        c = s[i:i + 8]
        for b in c:
            if b == 'I':
                a += t
            t //= 2

        yield chr(a)


for t in range(int(input())):
    input()
    s = input()

    print(f'Case #{t + 1}: {"".join(list(google(s)))}')
