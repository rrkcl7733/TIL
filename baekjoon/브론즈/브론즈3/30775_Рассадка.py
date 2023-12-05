m, k = map(int, input().split())
a = sum(map(int, input().split()))
x = a // m
if a % m:
  x += 1
print(x)
