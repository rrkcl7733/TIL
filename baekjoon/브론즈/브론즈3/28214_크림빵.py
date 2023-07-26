n, m, p = map(int, input().split())
a = list(map(int, input().split()))
x = 0
for i in range(0, n * m, m):
    if a[i:i+m].count(0) < p:
        x += 1
print(x)
