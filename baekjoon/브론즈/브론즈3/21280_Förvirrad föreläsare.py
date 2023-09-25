n = int(input())
a = list(map(int, input().split()))
t, x, y = a[0], 0, 0
for i in range(1, n):
  if a[i] > t:
    y += a[i] - t
  else:
    x += t - a[i]
  t = a[i]
print(x, y)
