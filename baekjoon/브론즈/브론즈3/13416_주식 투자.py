for _ in range(int(input())):
    x = 0
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        x += max(0, a, b, c)
    print(x)
