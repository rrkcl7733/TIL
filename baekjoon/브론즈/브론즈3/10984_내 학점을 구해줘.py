for _ in range(int(input())):
    n = x = 0
    for _ in range(int(input())):
        a, b = map(float, input().split())
        n += a
        x += a * b
    x /= n
    print(int(n), round(x, 1))
