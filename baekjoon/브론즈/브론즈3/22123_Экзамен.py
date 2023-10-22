def r(t):
  h, m, s = map(int, t.split(':'))
  return h * 60 + m + s / 60


for _ in range(int(input())):
  a, b, q = input().split()
  q = int(q)
  t = r(b) - r(a)
  if t <= 0:
    t += 1440
  print('Perfect' if q <= t else 'Test' if q <= t + 60 else 'Fail')
