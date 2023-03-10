n = int(input())
for i in range(n):
    x = ''
    if i % 2:
        for j in range(2 * n):
            if j % 2:
                x += '*'
            else:
                x += ' '
    else:
        for j in range(2 * n - 1):
            if j % 2:
                x += ' '
            else:
                x += '*'
    print(x)
