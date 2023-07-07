h, m = input().split(':')
h, m = int(h), int(m)
s = -m
m -= h
if s < 0:
  m -= 1
  s += 60
if m < 0:
  h -= 1
  m += 60
h, m, s = str(h), str(m), str(s)
h = h if len(h) > 1 else '0' + h
m = m if len(m) > 1 else '0' + m
s = s if len(s) > 1 else '0' + s
print(f'{h}:{m}:{s}')
