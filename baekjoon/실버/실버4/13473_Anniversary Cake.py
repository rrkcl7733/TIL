w, h, ax, ay, bx, by = map(int, input().split())
if ax == bx:
    print(0, ay, w, by)
else:
    print(ax, 0, bx, h)
