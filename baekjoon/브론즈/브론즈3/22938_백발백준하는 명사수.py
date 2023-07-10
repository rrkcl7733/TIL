x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())
t = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
print('YES' if t < r1 + r2 else 'NO')
