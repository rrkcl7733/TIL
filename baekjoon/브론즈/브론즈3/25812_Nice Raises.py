n, x = map(int, input().split())
a = b = 0
for _ in range(n):
  t = int(input())
  if t > x:
    b += 1
  elif x > t:
    a += 1
print(1 if a > b else 2 if b > a else 0)
