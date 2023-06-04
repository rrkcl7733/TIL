while 1:
    try:
        a = list(map(int, input().split()))
        n = len(a)
        x = [0] * n
        x[0], x[-1] = a[0] * a[1], a[n - 2] * a[-1]
        for i in range(1, n - 1):
            x[i] = a[i - 1] * a[i] * a[i + 1]
        print(*x)
    except:
        exit()
