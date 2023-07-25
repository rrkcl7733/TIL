a, b, v = map(int, input().split())
x = t = 0
while 1:
  t += a
  x += 1
  if t >= v:
    print(x)
    exit()
  t -= b
