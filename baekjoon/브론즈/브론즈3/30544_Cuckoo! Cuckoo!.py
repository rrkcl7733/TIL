h, m = input().split(':')
n = int(input())
h, m = int(h), int(m)
while 1:
  if not m:
    n -= h
  elif m in (0, 15, 30, 45):
    n -= 1
  if n < 1:
    break
  m += 1
  if m > 59:
    m = 0
    h += 1
  if h > 12:
    h = 1
print(f'{h:02d}:{m:02d}')
