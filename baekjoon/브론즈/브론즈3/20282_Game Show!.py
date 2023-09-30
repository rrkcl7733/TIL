n = int(input())
a = [int(input()) for _ in range(n)]
for i in range(n - 1):
  a[i + 1] += a[i]
print(max(max(a), 0) + 100)
