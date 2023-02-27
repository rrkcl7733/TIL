while 1:
    a, b, c, d = map(int, input().split())
    if (a, b, c, d) == (0, 0, 0, 0):
        exit()
    print(c - b, d - a)
