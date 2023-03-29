for _ in range(int(input())):
    a, b, c, d, q, w, e, r = map(int, input().split())
    print((1 if a + q < 1 else a + q) + 5 * (1 if b + w < 1 else b + w) + 2 * (0 if c + e < 0 else c + e) + 2 * (d + r))
