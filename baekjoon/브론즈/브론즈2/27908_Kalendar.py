def f(a):
    print(a, end='')


N, D = map(int, input().split())
d = 2 - D
t = '+---------------------+'
print(t)
f('|')
while 1:
    if d > N:
        if (d + D - 1) % 7 == 1:
            break
        while (d + D - 1) % 7 != 1:
            f('...')
            d += 1
        print('|')
        break

    if (d + D - 1) % 7 == 1 and d + D > 7:
        f('|')

    if d > 0:
        f('.' if d > 9 else '..')
        f(d)
    else:
        f('...')

    if (d + D - 1) % 7 == 0 and d + D > 7:
        print('|')

    d += 1
print(t)
