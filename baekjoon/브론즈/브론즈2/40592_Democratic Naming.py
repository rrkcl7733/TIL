n, m = map(int, input().split())
name = [list(input()) for _ in range(n)]
name = list(map(list, zip(*name)))
for i in range(m):
    d = dict()
    for j in range(n):
        d[name[i][j]] = d.get(name[i][j], 0) + 1
    k = sorted([k for k, v in d.items() if max(d.values()) == v])
    print(k[0], end='')
