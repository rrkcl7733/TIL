while 1:
    n, a, b = map(int, input().split())
    if (n, a, b) == (0, 0, 0):
        exit()
    t = n // 2
    print(0 if a > t else t - a + 1 if n - b > t else -1)
