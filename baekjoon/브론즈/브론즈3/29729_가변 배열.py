import sys


input = sys.stdin.readline
s, n, m = map(int, input().split())
t = 0
for _ in range(n + m):
  if int(input()):
    t += 1
    if t > s:
      s *= 2
  else:
    t -= 1
print(s)
