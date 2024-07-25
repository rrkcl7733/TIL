n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
t = []
for i in range(n):
    for j in range(m):
        if a[i][j] != '.':
            t.append((i, j))
for i, j in t:
    a[i][m - j - 1] = a[i][j]
for i in a:
    print(''.join(i))
