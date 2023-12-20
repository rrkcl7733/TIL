a, b = input().split(':')
c, d = input().split(':')
a, b, c, d = int(a), int(b), int(c), int(d)
if b < d or a < c:
  print('NO')
else:
  print('YES')
