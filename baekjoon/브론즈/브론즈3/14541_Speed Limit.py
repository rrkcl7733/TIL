while 1:
    n = int(input())
    if n == -1:
        exit()
    x = t = 0
    for _ in range(n):
        a, b = map(int, input().split())
        x += a * (b - t)
        t = b
    print(f'{x} miles')
