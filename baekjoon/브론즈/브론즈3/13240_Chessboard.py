n, m = map(int, input().split())
for i in range(n):
    print(*[['*', '.'][(i + j) % 2] for j in range(m)], sep='')
