while 1:
  n, m = map(int, input().split())
  if not n + m:
    break
  x = 0
  for i in map(int, input().split()):
    x += min(i, m // n)
  print(x)
