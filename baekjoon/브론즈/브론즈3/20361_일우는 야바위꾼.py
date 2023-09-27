n, x, k = map(int, input().split())
a = [0] * (n + 1)
a[x] = 1
for _ in range(k):
  i, j = map(int, input().split())
  a[i], a[j] = a[j], a[i]
print(a.index(1))
