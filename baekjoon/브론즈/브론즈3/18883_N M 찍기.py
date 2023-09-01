n, m = map(int, input().split())
for i in range(1, n * m + 1, m):
  print(*list(range(i, i + m)))
