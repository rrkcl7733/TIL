a = input()
x = 0
for i in range(16):
    t = int(a[i])
    if not i % 2:
        t *= 2
        if t > 9:
            t = t // 10 + t % 10
    x += t
print('NE' if x % 10 else 'DA')
