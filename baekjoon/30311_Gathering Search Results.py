n, k = map(int, input().split())
s = [0] * n
for _ in range(k):
    x = map(int, input().split())
    for i, y in enumerate(x):
        s[y-1] += i

s = [(s[i], i) for i in range(n)]
s.sort()
print(*[x[1] + 1 for x in s])
