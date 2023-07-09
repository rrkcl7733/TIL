d1, m1, y1, t = map(int, input().split())
d2, m2, y2 = map(int, input().split())
d2 -= d1
m2 -= m1
y2 -= y1
t -= 1
if d2 < 0:
    d2 += 30
    m2 -= 1
if m2 < 0:
    m2 += 12
    y2 -= 1
x = (y2 * 360 + m2 * 30 + d2) % 7
x = (t + x) % 7
print(x + 1)
