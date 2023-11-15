h1, d1, t1 = map(int, input().split())
h2, d2, t2 = map(int, input().split())
t = 0
h1 -= d2
h2 -= d1
while 1:
  if h1 <= 0 and h2 <= 0:
    print('draw')
    break
  elif h1 <= 0:
    print('player two')
    break
  elif h2 <= 0:
    print('player one')
    break
  t += 1
  if not t % t1:
    h2 -= d1
  if not t % t2:
    h1 -= d2
