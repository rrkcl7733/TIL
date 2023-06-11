n, m = map(int, input().split())
a = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    a[i] = (m - x) / y
print(a.index(min(a)) + 1)
