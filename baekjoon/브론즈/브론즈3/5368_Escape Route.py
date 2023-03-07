for _ in range(int(input())):
    n = int(input())
    a = [input() for _ in range(n)]
    p = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == 's':
                x, y = i, j
            elif a[i][j] == 'p':
                p.append((i, j))
    ans = 1e9
    xx = yy = 0
    for i, j in p:
        tmp = round(((x - i) ** 2 + (y - j) ** 2) ** .5, 2)
        if ans > tmp:
            ans = tmp
            xx, yy = i, j
    print(f'({x},{y}):({xx},{yy}):{ans:.2f}')
