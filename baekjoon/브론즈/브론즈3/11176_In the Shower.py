for _ in range(int(input())):
    e, n = map(int, input().split())
    x = 0
    for _ in range(n):
        if e < int(input()):
            x += 1
    print(x)
