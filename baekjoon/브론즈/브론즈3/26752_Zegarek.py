h, m, s = map(int, input().split())
s += 1
if s > 59:
    s = 0
    m += 1
if m > 59:
    m = 0
    h += 1
if h > 23:
    h = 0
h, m, s = str(h), str(m), str(s)
if len(h) < 2:
    h = '0' + h
if len(m) < 2:
    m = '0' + m
if len(s) < 2:
    s = '0' + s
print(f'{h}:{m}:{s}')
