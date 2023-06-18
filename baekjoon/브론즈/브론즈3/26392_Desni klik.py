n, r, s = map(int, input().split())
for _ in range(n):
    a = [input() for _ in range(r)]
    x = [0] * s
    for i in range(r):
        for j in range(s):
            if a[i][j] == '#':
                x[j] = r - i
    print(max(x) - min(x))
