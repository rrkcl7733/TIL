from itertools import combinations


pos = [[*map(int, input().split())] for _ in range(int(input()))]
ans = 0
for a, b, c in combinations(pos, 3):
    x1, x2, x3 = a[0], b[0], c[0]
    y1, y2, y3 = a[1], b[1], c[1]
    if len({x1, x2, x3}) != 3 and len({y1, y2, y3}) != 3:
        res = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        ans = max(ans, abs(res))
print(ans)
