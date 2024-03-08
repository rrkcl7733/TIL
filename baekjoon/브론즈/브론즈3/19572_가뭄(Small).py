d1, d2, d3 = map(int, input().split())
a = (d1 + d2 - d3) / 2
if 0 < a < d2 and d1 > a:
    b, c = d1 - a, d2 - a
    print(1)
    print("%.1f %.1f %.1f" % (a, b, c))
else:
    print(-1)
