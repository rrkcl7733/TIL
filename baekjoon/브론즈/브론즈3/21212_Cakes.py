x = 1e9
for _ in range(int(input())):
  a, b = map(int, input().split())
  x = min(x, b // a)
print(x)
