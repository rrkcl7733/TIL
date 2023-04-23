while 1:
    h1, m1, h2, m2 = map(int, input().split())
    if (h1, m1, h2, m2) == (0, 0, 0, 0):
        exit()
    if (h1 > h2) or (h1 == h2 and m1 > m2):
        h2 += 24
    print(m2 - m1 + 60 + (h2 - h1 - 1) * 60)
