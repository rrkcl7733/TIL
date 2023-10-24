n = input()
x = 'left' if (int(n[0]) + int(n[1])) % 2 else 'right'
print(x, int(n[2:]))
while 1:
    n = input()
    if n == '99999':
        break
    t = (int(n[0]) + int(n[1]))
    p = 'left' if t % 2 else 'right' if t > 0 else x
    print(p, int(n[2:]))
    x = p
